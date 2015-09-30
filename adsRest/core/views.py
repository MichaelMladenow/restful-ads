from django.shortcuts import render
from adsRest.utils import getPlayer
from adsRest.classes import Player

def show_player(request, tag = None, id = None):
    """A view of the player."""
    playerData = getPlayer(tag,id).json()
    stefan = Player(playerData)
    return render(request, 'base.html', {'playerData': stefan })