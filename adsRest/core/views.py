from django.shortcuts import render
from adsRest.utils import *
from adsRest.classes import Player, Paragon
from adsRest.constants import *


def show_player(request, tag=None, id=None, locale=None):
    """A view of the player. Includes:
        - Player name
        - Player guild
        - Player paragon
        - Player heroes
        - Hero Preview
    """
    locale = locale or 'eu'
    player_data = GetPlayer(tag, id, locale).json()

    if FetchSuccessful(player_data):
        #TODO: Export paragon fetch into utils, it's polluting the views :(
        player_paragon = Paragon(player_data['paragonLevel'], player_data['paragonLevelSeason'], player_data['paragonLevelSeasonHardcore'])

        player = Player(battle_tag = player_data['battleTag'],
                        paragon = player_paragon,
                        guild_name = player_data['guildName'],
                        heroes = ParseHeroes(player_data['heroes'], locale))
        return render(request, 'player.html', {'player_data': player})
    else:
        return render(request, 'notfound.html', {'error_data': Tag(tag,id)})



def search_player(request, locale=None):
    """The search view. Simple stuff. """
    locale = locale or 'eu'
    return render(request, 'search.html')

def show_hero(request, tag, id, hero_id, locale='eu'):
    locale = locale or 'eu'
    hero_data = GetHero(tag, id, hero_id, locale).json()
    return render(request, 'hero.html', {'hero_data': hero_data})
