import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Player(models.Model):
    player_text = models.CharField(max_length=200)

    def __str__(self):
        return self.player_text

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.team_name

class Match(models.Model):
    teams = models.ManyToManyField(Team)
    points_1 = models.IntegerField(default=0)
    points_2 = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def was_played_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
