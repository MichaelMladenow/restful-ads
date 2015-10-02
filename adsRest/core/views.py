from django.shortcuts import render
from adsRest.utils import getPlayer
from adsRest.classes import Player

def show_player(request, tag = None, id = None):
    """A view of the player."""
    playerData = getPlayer(tag,id).json()
    player = Player(battleTag = playerData['battleTag'], paragon=[], guildName = playerData['guildName'], heroes = playerData['heroes'])
    return render(request, 'base.html', {'playerData': player })

def search_player(request):
    """A view of the player."""
    return render(request, 'search.html')