from django.urls import path
from .import views

urlpatterns = [
    path('lost', views.lost_view, name = 'lost_view'),
    path('found', views.found_view, name = 'found_view'),
]