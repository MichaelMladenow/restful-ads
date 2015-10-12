from django.shortcuts import render
from adsRest.utils import GetPlayer, GetHero, ParseHeroes
from adsRest.classes import Player, Paragon
from adsRest.constants import *


def show_player(request, tag=None, id=None, locale=None):
    """A view of the player."""
    locale = locale or 'eu'
    player_data = GetPlayer(tag, id, locale).json()


    if 'code' in player_data.iterkeys() and player_data['code'] == 'NOTFOUND':
        """ Assert that the player was found """
        error_data = {
            'target': 'Player',
            'message': 'Player %s#%s could not be found in the %s servers.' % (tag, id, locale.upper())
        }
        return render(request, 'notfound.html', {'error_data': error_data})

    else:
        player_paragon = {
                    'normal': player_data['paragonLevel'],
                    'seasonal': player_data['paragonLevelSeason'],
                    'seasonal_hardcore': player_data['paragonLevelSeasonHardcore']
                }

        player = Player(battle_tag = player_data['battleTag'],
                        paragon = Paragon(player_paragon),
                        guild_name = player_data['guildName'],
                        heroes = ParseHeroes(player_data['heroes'], locale))
        return render(request, 'player.html', {'player_data': player})


def search_player(request, locale=None):
    """The search view. Simple stuff. """
    locale = locale or 'eu'
    return render(request, 'search.html')

def show_hero(request, tag, id, hero_id, locale='eu'):
    locale = locale or 'eu'
    hero_data = GetHero(tag, id, hero_id, locale).json()
    return render(request, 'hero.html', {'hero_data': hero_data})
