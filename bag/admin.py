# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import category,Image
# Register your models here.
admin.site.register(category)
admin.site.register(Image)