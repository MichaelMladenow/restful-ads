PAPERDOLL_URL = '/d3/static/images/profile/hero/paperdoll/'
BACKGROUND_URL = 'http://%s.battle.net/d3/static/images/hero/%s/bg.jpg'
HOST_URL = '.api.battle.net'

class Player(object):
    def __init__(self, battleTag, paragon, guildName, heroes):
        self.battle_tag = battleTag
        #TODO: PARAGONERINO
        self.paragon = Paragon(paragon['normal'], paragon['seasonal'], paragon['seasonalHardcore'])
        self.guild_name = guildName
        self.heroes = []
        for eachHero in heroes:
            tempHero = Hero(eachHero['name'], eachHero['level'], eachHero['paragonLevel'], eachHero['gender'], eachHero['class'], eachHero['id'])
            self.heroes.append(tempHero)

    def __str__(self):
        return self.battle_tag + ' Heroes : ' + self.__getHeroCount()

   	def _getHeroCount(self):
		return len(self.heroes)


class Hero(object):
    def __init__(self, name, level, paragon, gender, heroClass, heroID, region = "eu"):
        self.name = name
        self.level = level
        self.paragon = paragon
        self.gender = 'Male' if (gender == 0) else 'Female'
        self.heroClass = heroClass
        self.region = region
        self._id = heroID


	def classNameGet(self):
		return self.name

    def __str__(self):
        return '%d level %s' % (self.level, self.heroClass)

    def className(self, *args):
    	""" Get the class name 
			*possible params:
				'upper' - return the class name in upper case
				'lower' - return the class name in lower case
				'capitalize' - return the class name in capital case 
				'normalize' - cleans out the junk characters(dash '-')
			E.g. usage hero.getClassName('lower', 'normalize')
    	"""
    	name = self.heroClass.replace('-', ' ') if 'normalize' in args else self.heroClass 
    	if 'capitalize' in args:
    		return name.capitalize()
    	elif 'lower' in args:
    		return name.lower()
    	elif 'upper' in args:
    		return name.upper()
    	else:
			return self.className('capitalize', 'normalize')

    def getHeroId(self):
        return str(self._id)

    def getHeroBackground(self):
    	""" Returns absolute path to hero's background image """
    	return BACKGROUND_URL % (self.region, self.heroClass)

class Paragon(object):
    #TODO: Check normal hardcore
    def __init__(self, normal, seasonal, seasonalHardcore = None, normalHardcore = None):
        self.normal = normal
        self.seasonal = seasonal
        self.normalHardcore = normalHardcore
        self.seasonalHardcore = seasonalHardcore
        
    def __str__(self):
        output = 'Normal: %d, Seasonal: %d, Seasonal Hardcore: %d' % (self.normal, self.seasonal, self.seasonalHardcore)
        return output
