from django import template
from django.utils.html import format_html
from django.utils.text import gettext_lazy as _


register = template.Library() # Needed to access tags from template

@register.simple_tag
def cancel_button():
    """
    Function for custom tag to add a "Cancel" button in template form.
    :return: Str containing html code.
    """
    return format_html('<input type="button" value="'+_('Cancel')+'" onclick="history.back()">')
