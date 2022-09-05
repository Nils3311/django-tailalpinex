from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseNotFound


def index(request):
    return render(request, "app/example.html")


def index_htmx(request):
    if request.htmx:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return render(request, "app/example_htmx.html", {'time': current_time })
    else:
        return HttpResponseNotFound()
