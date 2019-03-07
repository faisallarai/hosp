from django.db import models

from oscar.apps.catalogue.abstract_models import ( 
    AbstractProduct,
    AbstractCategory
)

class Product(AbstractProduct):
    video_url = models.URLField(blank=True)
    out_of_stock = models.BooleanField(default=False) 
    markdown = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=True)
    short_description = models.CharField(max_length=120, blank=True)
    is_new = models.BooleanField(default=False)
    markdown_reason = models.CharField(max_length=120, blank=True)
    bestseller = models.BooleanField(default=False)

class Category(AbstractCategory):
    format_class = models.CharField(max_length=15, blank=True)

from oscar.apps.catalogue.models import *