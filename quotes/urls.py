"""
URL configuration for quotes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import quotecore.views

urlpatterns = [
    path('', quotecore.views.home, name='home'),
    path('about/', quotecore.views.about, name='about'),
    path('add-author/', quotecore.views.add_author, name='add-author'),
    path('add-category/', quotecore.views.add_category, name='add-category'),
    path('add-quote/', quotecore.views.add_quote, name='add-quote'),
    path('delete-author/<int:author_id>/', quotecore.views.delete_author, name='delete-author'),
    path('delete-category/<int:category_id>/', quotecore.views.delete_category, name='delete-category'),
    path('delete-quote/<int:quote_id>/', quotecore.views.delete_quote, name='delete-quote'),
    path('edit-author/<int:author_id>/', quotecore.views.edit_author, name='edit-author'),
    path('edit-category/<int:category_id>/', quotecore.views.edit_category, name='edit-category'),
    path('edit-quote/<int:quote_id>/', quotecore.views.edit_quote, name='edit-quote'),
    path('admin/', admin.site.urls),
    path('list-authors/', quotecore.views.list_authors, name='list-authors'),
    path('list-categories/', quotecore.views.list_categories, name='list-categories'),
    path('list-quotes/', quotecore.views.list_quotes, name='list-quotes'),
    path('list-quotes-author/<int:author_id>/', quotecore.views.list_quotes_author, name='list-quotes-author'),
    path('list-quotes-category/<int:category_id>/', quotecore.views.list_quotes_category, name='list-quotes-category'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('work-in-progress/', quotecore.views.work_in_progress, name='work-in-progress'),
]
