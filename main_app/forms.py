from django.forms import ModelForm
from .models import Battle, Move

class BattleForm(ModelForm):
    class Meta:
        model = Battle
        fields = ['date', 'enemy', 'result']

class MoveForm(ModelForm):
    class Meta:
        model = Move
        fields = ['name', 'type', 'power', 'accuracy', 'pp', 'category']