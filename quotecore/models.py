from django.db import models
from django.utils.text import gettext_lazy as _

class Author(models.Model):
    """
    Stores a single author.
    """
    first_name = models.CharField(max_length=128, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=128, verbose_name=_("Last Name"))
    pseudonym = models.CharField(max_length=128, blank=True, null=True, verbose_name=_("Pseudonym"))
    birth_date = models.DateTimeField(verbose_name=_("Birth Date"))
    death_date = models.DateTimeField(blank=True, null=True, verbose_name=_("Death Date"))

    class  Meta:
        """
        Class for ordering author by last name and then first name
        """
        ordering = [ 'last_name','first_name']


    def random_quote(self):
        """
        This function is used to generate a random quote.
        :return:
        """
        pass


    def __str__(self):
        """
        To string function for default display
        :return: string containing author last name, first name and pseudonym if author has one.
        """
        author_str = f"{self.last_name}, {self.first_name}" if self.pseudonym is None else f"{self.last_name}, {self.first_name} ({self.pseudonym})"
        return author_str


class Category(models.Model):
    """
    Stores a single categories related to :model:`quotequore.Quote`.
    """
    label = models.CharField(max_length=128, verbose_name=_("Label"))

    class Meta:
        """
        Class used to ordering categories by label
        """
        ordering = [ 'label' ]

    def __str__(self):
        """
        To string function for label default display
        :return:
        """
        return self.label


class Quote(models.Model):
    """
    Stores a single quote.
    """
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name=_('quotes'), verbose_name=_("Authors"))
    category = models.ManyToManyField(Category)
    source = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("Source"))
    text = models.CharField(max_length=1024, verbose_name=_("Text"))
