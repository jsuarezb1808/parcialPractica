from django.shortcuts import render # here by default
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect,render,get_object_or_404
from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class HomePageView(TemplateView):
    template_name ='pages/base.html'