from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Tool

def index(request, selection=None):

    types = ['Yard', 'Woodworking', 'Plumbing', 'Auto']

    if selection == None:
        tool_list = Tool.objects.all()

    else:
        tool_list = Tool.objects.filter(types=selection.upper())

    context = {
        'tool_list': tool_list,
        'types': types
    }
    return render(request, 'hey_neighbor/index.html', context)
