from django import forms
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
