from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('subway/', views.subway_form),
    path('subway_result/', views.subway_result),
    path('subway/<int:id>/', views.subway_id),
]