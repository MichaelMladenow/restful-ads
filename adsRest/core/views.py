from django.shortcuts import render
from adsRest.utils import getPlayer
from adsRest.classes import Player


def show_player(request, tag=None, id=None):
    """A view of the player."""

    playerData = getPlayer(tag, id).json()
    playerParagon = {'normal': playerData['paragonLevel'],
                     'seasonal': playerData['paragonLevelSeason'],
                     'seasonalHardcore': playerData['paragonLevelSeasonHardcore']
                    }

    player = Player(battleTag = playerData['battleTag'],
                    paragon = playerParagon,
                    guildName = playerData['guildName'],
                    heroes = playerData['heroes'])
    return render(request, 'base.html', {'playerData': player,
                  'debugData': playerData})


def search_player(request):
    """The search viw."""

    return render(request, 'search.html')



