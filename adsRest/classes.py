class Player(object):
    def __init__(self, data=None):
    	self.battle_tag = data['battleTag']
    	self.paragon_level = data['paragonLevel']
    	self.paragon_level_season = data['paragonLevelSeason']
    	self.guild_name = data['guildName']
    	self.heroes = []
    	for eachHero in data['heroes']:
   			self.heroes.append(Hero(eachHero))


class Hero(object):
    def __init__(self, data=None):
		self.name = data['name']
		self.level = data['level']
		self.paragon_level = data['paragonLevel']
		self.gender = data['gender']
		self.heroClass = data['class']


