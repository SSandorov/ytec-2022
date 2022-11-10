from django import forms
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import Player, Team, Match
# from .forms import PlayerForm
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'soccer/index.html'
    context_object_name = 'player_list'

# def index(request):
#     player_list = Player.objects.order_by('-id')
#     context = {'player_list': player_list}
#     return render(request, 'soccer/index.html', context)
    def get_queryset(self):
        return Player.objects.order_by('-id')

def playersList(request):
    text = 'Hey!'
    return HttpResponse(text)

class CreatePlayer(CreateView):
    model = Player
    template_name = 'soccer/create-player.html'
    fields = ['player_text']
    # success_url: reverse_lazy('create-player')

class TeamsView(generic.ListView):
    template_name = 'soccer/teams.html'
    context_object_name = 'team_list'
# def teams(request):
#     team_list = Team.objects.order_by('-id')
#     # output = ', '.join([t.team_name for t in team_list])
#     # return HttpResponse(output)
#     context = {'team_list': team_list}
#     return render(request, 'soccer/teams.html', context)
    def get_queryset(self):
        return Team.objects.order_by('-id')


class MatchesView(generic.ListView):
    template_name = 'soccer/matches.html'
    context_object_name = 'match_list'

    # def matches(request):
    # match_list = Match.objects.all().order_by('-id')
    # context = {'match_list': match_list}
    # return render(request, 'soccer/matches.html', context)
    def get_queryset(self):
        return Match.objects.all().order_by('-id')

class ResultsView(generic.DetailView):
    model = Team
    template_name = 'soccer/results.html'
# def results(request, team_id):
#     team = get_object_or_404(Team, pk=team_id)
#     return render(request, 'soccer/results.html', {'team': team})