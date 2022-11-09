from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Player, Team, Match
# Create your views here.


def index(request):
    team_list = Team.objects.order_by('id')
    # output = ', '.join([t.team_name for t in team_list])
    # return HttpResponse(output)
    context = {'team_list': team_list}
    return render(request, 'soccer/index.html', context)

def results(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'soccer/results.html', {'team': team})