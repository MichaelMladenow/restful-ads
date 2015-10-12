import requests
from adsRest.constants import *

def GetPlayer(tag, id, locale, params = BASE_PARAMS):
	""" Fetch player data by battle tag """
	battle_tag = '%s-%s' % (tag, id)
	raw_url = ((BASE_URL % locale) + (PLAYER_SUFFIX % battle_tag))
	req_url = _appendParams(raw_url, params)
	return requests.get(req_url)

def GetHero(player_tag, heroId, locale, params = BASE_PARAMS):
    battle_tag = '%s-%s' % (tag, id)
    raw_url = ((BASE_URL % locale) + (PLAYER_SUFFIX % player_tag) + '/' + heroId)
    req_url = _appendParams(raw_url, params)


def _appendParams(url, params):
	""" Append parameters to the end of the get string url """
	output_url = url
	isFirstParam = True
	for eachKey in params.iterkeys():
		prefix_symbol = '?' if isFirstParam else '&'
		output_url += ('%s%s=%s' % (prefix_symbol, eachKey, params[eachKey]))
		if isFirstParam:
			isFirstParam = False
	return output_url
