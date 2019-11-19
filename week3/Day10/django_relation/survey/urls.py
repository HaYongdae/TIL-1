from django.urls import path
from . import views

app_name = "survey"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('<int:q_id>/', views.detail, name="detail"),
    path('<int:q_id>/edit/', views.edit, name="edit"),
    path('<int:q_id>/delete/', views.delete, name="delete"),

    path('<int:q_id>/survey/', views.survey, name="survey"),
    path('<int:c_id>/survey_edit/', views.survey_edit, name="survey_edit"),
    path('<int:c_id>/survey_delete/', views.survey_del, name="sur_del"),
    path('<int:c_id>/vote/', views.vote, name="vote"),
]