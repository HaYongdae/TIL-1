from django.urls import path
from . import views

app_name="subway"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('detail/<int:s_id>/', views.detail, name="detail"),
    path('edit/<int:s_id>/', views.edit, name="edit"),
    path('delete/<int:s_id>/', views.delete, name="delete"),
]
