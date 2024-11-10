from django.apps import AppConfig


class QuotecoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quotecore'
    developers = 'Franck GERVAIS'
    license = 'GPL3'
    pagination_size = 20
    repository = 'https://github.com/FGE18/quotes'
    version = '0.4.0'
