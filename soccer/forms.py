from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Player, Team, Match

# class PlayerForm(forms.Form):
#         player = forms.CharField(max_length=200)

#         def clean_player(self):
#             text = self.cleaned_data['player']

#             if (len(text) == 0):
#                 raise ValidationError(_('No player was submited'))
        
#             return text
# class PlayerForm(ModelForm):
#     class Meta:
#         model = Player
#         fields = ['player_text']
