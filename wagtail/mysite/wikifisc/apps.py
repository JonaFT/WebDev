from django.apps import AppConfig


class WikifiscConfig(AppConfig):
    name = 'wikifisc'
    default_site = 'wikifisc.sites.MyWikiSite'
