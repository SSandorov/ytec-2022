from django.urls import path

from . import views

app_name = 'soccer'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-player', views.CreatePlayer.as_view(), name = 'create-player'),
    path('teams', views.TeamsView.as_view(), name='teams'),
    path('matches', views.MatchesView.as_view(), name='matches'),
    path('teams/<int:pk>/', views.ResultsView.as_view(), name='results'),
    path('players', views.playersList, name='players')
]