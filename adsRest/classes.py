class Player(object):
    def __init__(self, battleTag, paragon, guildName, heroes):
    	self.battle_tag = battleTag
    	#TODO: PARAGONERINO
    	self.guild_name = guildName
    	self.heroes = []
    	for eachHero in heroes:
			tempHero = Hero(eachHero['name'], eachHero['level'], [], eachHero['gender'], eachHero['class'])
			self.heroes.append(tempHero)

   	def __str__(self):
   		return self.battle_tag + ' Heroes : ' + self.__getHeroCount()

   	def _getHeroCount(self):
   		return len(self.heroes)


class Hero(object):
    def __init__(self, name, level, paragonLevel, gender, heroClass):
		self.name = name
		self.level = level
		self.paragon_level = paragonLevel
		self.gender = gender
		self.heroClass = heroClass

    def __str__(self):
		return '%d level %s' % (self.level, self.heroClass)

class Paragon(object):
	def __init__(self, normal, seasonal, normalHardcore = None, seasonalHardcore = None):
		self.normal = normal
		self.seasonal = seasonal
		self.normalHardcore = normalHardcore
		selfs.seasonalHardcore = seasonalHardcore
	def __str__(self):
		output = 'Normal level: %d, Seasonal level: %d, Normal Harcore level: %d, Seasonal Hardcore level: %d'	% (self.normal, self.seasonal, self.normalHardcore, self.seasonalHardcore)
