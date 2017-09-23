# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from person.models import Person, Identification
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from person.serializers import PersonSerializer


# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
