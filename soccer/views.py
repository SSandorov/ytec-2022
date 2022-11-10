from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.views import generic

from .models import Player, Team, Match
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'soccer/index.html'
    context_object_name = 'player_list'

    def get_queryset(self):
        return Player.objects.order_by('-id')

def playersList(request):
    text = 'Hey!'
    return HttpResponse(text)

class CreatePlayer(CreateView):
    model = Player
    template_name = 'soccer/create-player.html'
    fields = ['player_text']

class TeamsView(generic.ListView):
    template_name = 'soccer/teams.html'
    context_object_name = 'team_list'

    def get_queryset(self):
        return Team.objects.order_by('-id')

class CreateTeam(CreateView):
    model = Team
    template_name = 'soccer/create-team.html'
    fields = ['team_name', 'players']

class MatchesView(generic.ListView):
    template_name = 'soccer/matches.html'
    context_object_name = 'match_list'

    def get_queryset(self):
        return Match.objects.all().order_by('-id')

class CreateMatch(CreateView):
    model = Match
    template_name = 'soccer/create-match.html'
    fields = ['teams', 'points_1', 'points_2', 'pub_date']

class ResultsView(generic.DetailView):
    model = Team
    template_name = 'soccer/results.html'