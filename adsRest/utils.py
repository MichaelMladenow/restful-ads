import requests
""" CONSTANTS::START """
BASE_URL = 'https://eu.api.battle.net/d3/'
PLAYER_SUFFIX = 'profile/%s/'
HERO = 'player/%s/hero/%s/'
BASE_PARAMS = {
	'locale' : 'en_GB',
	'apikey' : 'ar23bkxhcjssvhpa6b752v4zxgdvd3j3',
}
""" CONSTANTS::END """

def getPlayer(tag, id, params = BASE_PARAMS):
	""" Fetch player data by battle tag """
	battle_tag = '%s-%s' % (tag, id)
	raw_url = (BASE_URL + (PLAYER_SUFFIX % battle_tag))
	req_url = appendParams(raw_url, params)
	return requests.get(req_url)


def appendParams(url, params):
	""" Append parameters to the end of the get string url """
	output_url = url
	isFirstParam = True
	for eachKey in params.iterkeys():
		prefix_symbol = '?' if isFirstParam else '&'
		output_url += ('%s%s=%s' % (prefix_symbol, eachKey, params[eachKey]))
		if isFirstParam:
			isFirstParam = False
	return output_url

def getHeroImage(hero):
	#TODO: GET THE FUCKING HERO IMG