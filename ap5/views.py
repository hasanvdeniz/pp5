from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def second(request):
  template = loader.get_template('second.html')
  return HttpResponse(template.render({}, request))

def third(request):
  template = loader.get_template('third.html')
  return HttpResponse(template.render({}, request))

def secondsecond(request):
  template = loader.get_template('secondsecond.html')
  return HttpResponse(template.render({}, request))
