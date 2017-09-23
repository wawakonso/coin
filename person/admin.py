# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from person.models import Person, Identification

admin.site.register(Person)
admin.site.register(Identification)
# Register your models here.
