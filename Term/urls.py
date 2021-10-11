from django.urls import path
from . import views
from .models import Term

urlpatterns = [

    path('', views.term, name="term"),
    
    path('delete-term/<str:pk>/', views.delete_term, name="delete_term"),

    path('edit-term/<str:pk>/', views.edit_term, name="edit_term"),

    path('vocabulary/<int:pk>/', views.vocabulary, name="vocabulary"),

    path('delete-vocabulary/<str:pk>/', views.delete_vocabulary, name="delete_vocabulary"),

    path('update-vocabulary/<str:pk>/', views.update_vocabulary, name="update_vocabulary")

]
