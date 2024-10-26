from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import gettext_lazy as _
from quotecore.forms import QuoteForm, CategoryForm, AuthorForm
from quotecore.models import Author, Category, Quote


# Authors pages
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
            if form.save():
                messages.success(request, _("Author added successfully"))
            else:
                messages.error(request, _("Unable to save author in database"))
            return redirect("add-author")
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})


@login_required
def delete_author(request, author_id):
    """
    Function to delete a single author identified by its ID.
    :param request:
    :param author_id: int Author id to delete
    :return:
    """
    author = get_object_or_404(Author, id=author_id)
    delete_form = AuthorForm(instance=author)
    if request.method == 'POST':
        delete_form = AuthorForm(request.POST, instance=author)
        if delete_form.is_valid():
            if author.delete():
                messages.success(request, _("Author deleted successfully"))
                return redirect("list-authors")
            else:
                messages.error(request, _("Unable to delete author in database"))
    return render(request, 'delete_author.html', {'delete_form': delete_form, 'author': author})


@login_required
def edit_author(request, author_id):
    """
    Function to edit a single author identified by its ID.
    :param request:
    :param author_id: int Author id to edit
    :return:
    """
    author = get_object_or_404(Author, id=author_id)
    edit_form = AuthorForm(instance=author)
    if request.method == 'POST':
        edit_form = AuthorForm(request.POST, instance=author)
        if edit_form.is_valid():
            if edit_form.save():
                messages.success(request, _("Author saved successfully"))
                return redirect("list-authors")
            else:
                messages.error(request, _("Unable to save author in database"))
    return render(request, 'edit_author.html', {'edit_form': edit_form})


def list_authors(request):
    """
    Lists all authors in the database.
    :param request:
    :return:
    """
    authors = Author.objects.all().order_by('last_name', 'first_name')
    return render(request, 'list_authors.html', {'authors': authors})


# Categories pages
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
            if form.save():
                messages.success(request, _("Category added successfully"))
            else:
                messages.error(request, _("Unable to save category in database"))
            return redirect("add-category")
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


@login_required
def delete_category(request, category_id):
    """
    Function to delete a single category identified by its ID.
    :param request:
    :param category_id: int Category id to delete
    :return:
    """
    category = get_object_or_404(Category, id=category_id)
    delete_form = CategoryForm(instance=category)
    if request.method == 'POST':
        delete_form = CategoryForm(request.POST, instance=category)
        if delete_form.is_valid():
            if category.delete():
                messages.success(request, _("Category deleted successfully"))
                return redirect("list-categories")
            else:
                messages.error(request, _("Unable to delete category in database"))
    return render(request, 'delete_category.html', {'delete_form': delete_form, 'category': category})


@login_required
def edit_category(request, category_id):
    """
    Function to edit a single quote identified by its ID.
    :param request:
    :param category_id: int Category ID to edit
    :return:
    """
    category = get_object_or_404(Category, id=category_id)
    edit_form = CategoryForm(instance=category)
    if request.method == 'POST':
        edit_form = CategoryForm(request.POST, instance=category)
        if edit_form.is_valid():
            if edit_form.save():
                messages.success(request, _("Category saved successfully"))
                return redirect("list-categories")
            else:
                messages.error(request, _("Unable to save category in database"))
    return render(request, 'edit_category.html', {'edit_form': edit_form})


def list_categories(request):
    """
    Lists all categories stored in database.
    :param request:
    :return:
    """
    categories = Category.objects.all().order_by('label')
    return render(request, 'list_categories.html', {'categories': categories})


# Quotes pages
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
            if form.save():
                messages.success(request, _("Quote added successfully"))
            else:
                messages.error(request, _("Unable to save quote in database"))
            return redirect("add-quote")
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})


@login_required
def delete_quote(request, quote_id):
    """
    Function to delete a single quote identified by its ID.
    :param request:
    :param quote_id: int Quote id to delete
    :return:
    """
    quote = get_object_or_404(Quote, id=quote_id)
    delete_form = QuoteForm(instance=quote)
    if request.method == 'POST':
        delete_form = QuoteForm(request.POST, instance=quote)
        if delete_form.is_valid():
            if quote.delete():
                messages.success(request, _("Quote deleted successfully"))
                return redirect("list-quotes")
            else:
                messages.error(request, _("Unable to delete quote in database"))
    return render(request, 'delete_quote.html', {'delete_form': delete_form, 'quote': quote})


@login_required
def edit_quote(request, quote_id):
    """
    Function to edit a single quote identified by its ID.
    :param request:
    :param quote_id: int Author id to edit
    :return:
    """
    quote = get_object_or_404(Quote, id=quote_id)
    edit_form = QuoteForm(instance=quote)
    if request.method == 'POST':
        edit_form = QuoteForm(request.POST, instance=quote)
        if edit_form.is_valid():
            if edit_form.save():
                messages.success(request, _("Quote saved successfully"))
                return redirect("list-quotes")
            else:
                messages.error(request, _("Unable to save quote in database"))
    return render(request, 'edit_quote.html', {'edit_form': edit_form})


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


# Site pages
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
