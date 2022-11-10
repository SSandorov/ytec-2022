from django.urls import path

from . import views

app_name = 'soccer'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.PlayersView.as_view(), name='players'),
    path('players/add', views.CreatePlayer.as_view(), name = 'create-player'),
    path('teams', views.TeamsView.as_view(), name='teams'),
    path('teams/add', views.CreateTeam.as_view(), name='create-team'),
    path('matches', views.MatchesView.as_view(), name='matches'),
    path('matches/add', views.CreateMatch.as_view(), name='create-match'),
    path('teams/<int:pk>/', views.ResultsView.as_view(), name='results'),
    path('players', views.playersList, name='players')
]