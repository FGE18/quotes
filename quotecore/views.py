from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from quotecore.forms import QuoteForm, CategoryForm, AuthorForm
from quotecore.models import Author, Category, Quote


def about(request):
    """
    Function for displaying application information in about page.
    :param request:
    :return:
    """
    context = {
        'app_developers':apps.get_app_config('quotecore').developers,
        'app_license':apps.get_app_config('quotecore').license,
        'app_repository':apps.get_app_config('quotecore').repository,
        'app_version': apps.get_app_config('quotecore').version,
    }
    return render(request, 'about.html', context= context)


@login_required
def add_author(request):
    """
    Adds a new author in the database. After creation user is redirected to a new empty form.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add-author")
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


def list_authors(request):
    """
    Lists all authors in the database.
    :param request:
    :return:
    """
    authors = Author.objects.all().order_by('last_name', 'first_name')
    return render(request, 'list_authors.html', {'authors': authors})


@login_required
def add_category(request):
    """
    Adds a new category in the database. After creation user is redirected to a new empty form.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add-category")
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


def list_categories(request):
    """
    Lists all categories stored in database.
    :param request:
    :return:
    """
    categories = Category.objects.all().order_by('label')
    return render(request, 'list_categories.html', {'categories': categories})


@login_required
def add_quote(request):
    """
    Add a new quote in the database. After creation user is redirected to a new empty form.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add-quote")
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})


def list_quotes(request):
    """
    List all quotes stored in database.
    :param request:
    :return:
    """
    quotes = Quote.objects.all().order_by('author')
    authors = Author.objects.all()
    return render(request, 'list_quotes.html', {'quotes': quotes, 'authors': authors})


def list_quotes_author(request, author_id):
    """
    List all quotes for an author entered in parameter in the database.
    :param request:
    :param author_id: ID of the author
    :return:
    """
    quotes = Quote.objects.filter(author=author_id)
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'list_quotes_author.html', {'quotes': quotes, 'author': author})


def list_quotes_category(request, category_id):
    """
    List all quotes for a category entered in parameter in the database.
    :param request:
    :param category_id: ID of the category
    :return:
    """
    quotes = Quote.objects.filter(category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    authors = Author.objects.all()
    context = {'quotes': quotes, 'category': category, 'authors': authors}
    return render(request, 'list_quotes_category.html', context)


def home(request):
    """
    Application home page. This page returns the last 5 quotes added.
    :param request:
    :return:
    """
    quotes = Quote.objects.all().order_by('-id')[:5]
    return render(request, 'home.html', {'quotes': quotes})


def work_in_progress(request):
    """
    Temporary function for work in progress page.
    :param request:
    :return:
    """
    return render(request, 'work_in_progress.html')
