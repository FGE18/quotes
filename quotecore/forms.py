from django import forms
from django.utils.text import gettext_lazy as _
from . import models

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'


class QuoteForm(forms.ModelForm):
    class Meta:
        model = models.Quote
        fields = '__all__'


class SearchForm(forms.Form):
    search_string = forms.CharField(label=_("Tag for search"), max_length=64, required=True)
