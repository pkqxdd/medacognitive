from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404

def home(request):
    return HttpResponseRedirect('/hospital')


def hospital(request):
    pass
