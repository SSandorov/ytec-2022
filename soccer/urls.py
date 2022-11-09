from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams', views.teams, name='teams'),
    path('matches', views.matches, name='matches'),
    path('teams/<int:team_id>/', views.results, name='results')
]