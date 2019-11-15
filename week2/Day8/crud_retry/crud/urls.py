from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
    path('<int:id>/detail/', views.detail),
    path('<int:id>/update/', views.update),
    path('<int:id>/save/', views.arti_save),
    path('<int:id>/delete/', views.delete),
]