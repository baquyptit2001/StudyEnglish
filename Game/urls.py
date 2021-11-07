from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="game.home"),
    path('add_question/', views.add_question, name="game.add"),
]
