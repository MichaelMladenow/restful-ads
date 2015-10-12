from django.shortcuts import render
from adsRest.utils import GetPlayer
from adsRest.classes import Player
from adsRest.constants import *


def show_player(request, tag=None, id=None, locale=None):
    """A view of the player."""
    locale = locale or 'eu'
    player_data = GetPlayer(tag, id, locale).json()


    if 'code' in player_data.iterkeys() and player_data['code'] == 'NOTFOUND':
        """ Assert that the player was found """
        error_data = {
            'target': 'Player',
            'message': 'Player %s#%s could not be found in the %s servers.' % (tag, id, locale.upper())}
        return render(request, 'notfound.html', {'error_data': error_data})

    else:
        player_paragon = {'normal': player_data['paragonLevel'],
                         'seasonal': player_data['paragonLevelSeason'],
                         'seasonal_hardcore': player_data['paragonLevelSeasonHardcore']
                        }

        player = Player(battleTag = player_data['battleTag'],
                        paragon = player_paragon,
                        guildName = player_data['guildName'],
                        heroes = player_data['heroes'])
        return render(request, 'base.html', {'player_data': player,
                      'debugData': dir(player.heroes[0]),
                      'locDebug': locale})


def search_player(request, locale='eu'):
    """The search view."""

    return render(request, 'search.html', {'locDebug': locale})

def show_hero(requst, playerTag, heroID, locale='eu'):
    return false

