from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context,Template

# Create your views here.


def hello(request):
    html = {'mars': 'mars', 'day': 'saturday', 'user': 'john',}
    return render(request, 'myWeb/index.html', html)


def current_date(request):
    html = {'mars': 'mars', }
    return render(request, 'myWeb/date.html', html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise ValueError
    html = "<html><body>It is now %s.</body></html>" %offset
    return HttpResponse(html)