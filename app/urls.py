from django.urls import path

from . import views

urlpatterns = [
    path('htmx', views.index, name='index'),
    path('htmx_time', views.index_htmx, name='index_htmx'),
]