from django.db import models

# Create your models here.

"""Flexible page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class Wiki(Page):
    """Flexibile page class."""

    template = "wiki/base.html"

    # @todo add streamfields 
    # content = StreamField()

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:  # noqa 
        verbose_name = "Wiki page"
        verbose_name_plural = "Wiki Pages"