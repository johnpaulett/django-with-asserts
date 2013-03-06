try:
    from django.conf.urls import patterns, url
except ImportError:
    # Django 1.3 stored patterns in the defaults module, deprecated as of 1.5
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'simple.views',
    url(r'^template/(?P<template_name>[\w\-_]+)/$', 'template'),
    url(r'^echo/((?P<status>\d{3})/)?$', 'echo'),
)
