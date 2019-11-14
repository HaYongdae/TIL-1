from django.urls import path
from . import views

urlpatterns = [
    path('font/', views.google_font),
]