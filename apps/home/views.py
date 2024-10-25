# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout  # Correctly import the logout function
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    # Context data for the template
    context = {'segment': 'index'}

    # Load the index.html template and render it
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    # Context dictionary
    context = {}

    # Extract the HTML file name from the URL
    load_template = request.path.split('/')[-1]

    # If the URL points to the admin page, redirect to the Django admin dashboard
    if load_template == 'admin':
        return HttpResponseRedirect(reverse('admin:index'))

    # Set the segment for the template
    context['segment'] = load_template

    # Load the corresponding HTML template based on the URL
    html_template = loader.get_template('home/' + load_template)
    return HttpResponse(html_template.render(context, request))


def current(request):
    return render(request, 'home/current.html')


def historical(request):
    return render(request, 'home/historical.html')



