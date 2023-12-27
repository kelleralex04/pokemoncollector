from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Pokemon, Move
from .forms import BattleForm
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {
        'pokemon': pokemon
    })

def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    id_list = pokemon.moves.all().values_list('id')
    unknown_moves = Move.objects.exclude(id__in=id_list)
    battle_form = BattleForm()
    return render(request, 'pokemon/detail.html', {
        'pokemon': pokemon, 'battle_form': battle_form,
        'moves': unknown_moves
    })

def add_battle(request, pokemon_id):
    form = BattleForm(request.POST)
    if form.is_valid():
        new_battle = form.save(commit=False)
        new_battle.pokemon_id = pokemon_id
        new_battle.save()
    return redirect('detail', pokemon_id=pokemon_id)

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    success_url = '/pokemon'

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['type', 'trainer']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemon'

class MoveList(ListView):
    model = Move

class MoveDetail(DetailView):
    model = Move

class MoveUpdate(UpdateView):
    model = Move
    fields = ['name', 'type', 'power', 'accuracy', 'pp', 'category']

class MoveDelete(DeleteView):
    model = Move
    success_url = '/moves'

class MoveCreate(CreateView):
    model = Move
    fields = '__all__'
    success_url = '/moves'

def assoc_move(request, pokemon_id, move_id):
    Pokemon.objects.get(id=pokemon_id).moves.add(move_id)
    return redirect('detail', pokemon_id=pokemon_id)