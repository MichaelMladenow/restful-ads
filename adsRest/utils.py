import requests
from adsRest.constants import *
from adsRest.classes import *

def GetPlayer(tag, player_id, locale, params = BASE_PARAMS):
	""" Fetch player data by battle tag """
	battle_tag = Tag(tag, player_id)
	raw_url = ((BASE_URL % locale) + (PLAYER_SUFFIX % battle_tag))
	req_url = _appendParams(raw_url, params)
	return requests.get(req_url)

def GetHero(tag, player_id, hero_id, locale, params = BASE_PARAMS):
    """ Fetch hero by id and player battle tag """
    battle_tag = Tag(tag, player_id)
    raw_url = (BASE_URL + HERO_SUFFIX) % (locale, battle_tag, hero_id)
    req_url = _appendParams(raw_url, params)
    return requests.get(req_url)

def _appendParams(url, params):
	""" Append parameters to the end of the query string @url """
	output_url = url
	isFirstParam = True
	for eachKey in params.iterkeys():
		prefix_symbol = '?' if isFirstParam else '&'
		output_url += ('%s%s=%s' % (prefix_symbol, eachKey, params[eachKey]))
		if isFirstParam:
			isFirstParam = False
	return output_url

def ParseHero(hero, localization):
    try:
        character = Hero(
                name = hero['name'],
                level = hero['level'],
                paragon = hero['paragonLevel'],
                gender = hero['gender'],
                hero_class = hero['class'],
                hero_id = hero['id'],
                seasonal = hero['seasonal'],
                hardcore = hero['hardcore'],
                locale = localization)
        return character
    except Exception as err:
        raise AssertionError('Could not make a hero out of %s. Error: %s' % (hero, err.message))

def ParseHeroes(hero_list, localization):
    heroes = []
    for each_hero in hero_list:
        heroes.append(ParseHero(each_hero, localization))
    return heroes

def Tag(name, player_id, separator='-'):
    return name + separator + player_id