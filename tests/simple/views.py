from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


@require_POST
def echo(request, status=200):
    return HttpResponse(request.body, status=status)


def template(request, template_name):
    # Don't do this in real-life (server file path from user), but makes
    # testing easier to let test pick the HTML to render
    return render(request, 'tests/{0}.html'.format(template_name))
