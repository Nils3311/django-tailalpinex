import os
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseNotFound

testvariable = os.environ.get('test', None)

def index(request):
    return render(request, "app/example.html")


def index_htmx(request):
    if request.htmx:
        now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        current_time = testvariable
        return render(request, "app/example_htmx.html", {'time': current_time})
    else:
        return HttpResponseNotFound()
