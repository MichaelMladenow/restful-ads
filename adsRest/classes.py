from adsRest.constants import *

class Player(object):
    """ A player | D3 BattleNET account """
    def __init__(self, battle_tag, paragon, guild_name, heroes):
        self.battle_tag = battle_tag
        self.paragon = paragon
        self.guild_name = guild_name
        self.heroes = []
        self.AddHeroes(heroes)

    def __str__(self):
        return self.battle_tag + ' Heroes : ' + self.__getHeroCount()

   	def _getHeroCount(self):
        """ Returns the amount of heroes this player has """
		return len(self.heroes)

    def AddHero(self, hero):
        """ Assign a hero to a player """
        if isinstance(hero, Hero):
            self.heroes.append(hero)
        else:
            raise AssertionError('%s is not a valid hero. Could not add to hero list.' % hero)

    def AddHeroes(self, hero_list):
        """ Assign multiple heroes to a player """
        for each_hero in hero_list:
            self.AddHero(each_hero)

class Hero(object):
    """ Diablo 3 Hero """
    def __init__(self, name, level, paragon, gender, hero_class, hero_id, seasonal, hardcore, locale):
        self.name = name
        self.level = level
        self.paragon = paragon
        self.gender = 'Male' if (gender == 0) else 'Female'
        self.hero_class = hero_class
        self._id = hero_id
        self.is_seasonal = seasonal
        self.is_hardcore = hardcore
        self.locale = locale

	def ClassName(self):
        """ Get a hero's classname """
		return self.name

    def __str__(self):
        return '%d level %s' % (self.level, self.hero_class)

    def className(self, *args):
    	""" Get the class name 
			*possible params:
				'upper' - return the class name in upper case
				'lower' - return the class name in lower case
				'capitalize' - return the class name in capital case 
				'normalize' - cleans out the junk characters(dash '-')
			E.g. usage hero.getClassName('lower', 'normalize')
    	"""
    	name = self.hero_class.replace('-', ' ') if 'normalize' in args else self.hero_class 
    	if 'capitalize' in args:
    		return name.capitalize()
    	elif 'lower' in args:
    		return name.lower()
    	elif 'upper' in args:
    		return name.upper()
    	else:
			return self.className('capitalize', 'normalize')

    def getHeroId(self):
        """ TODO: Restrict access """
        return str(self._id)

    def Portrait(self):
    	""" Returns absolute path to hero's background image
            Based on hero's class and region
        """
    	return BACKGROUND_URL % (self.locale, self.hero_class)

class Paragon(object):
    """ Paragon levels """
    """ TODO: Improve Paragon structure/assignment """
    def __init__(self, normal, seasonal, seasonal_hardcore = None, normal_hardcore = None):
        self.normal = normal
        self.seasonal = seasonal
        self.normal_hardcore = normal_hardcore
        self.seasonal_hardcore = seasonal_hardcore
        
    def __str__(self):
        output = 'Normal: %d, Seasonal: %d, Seasonal Hardcore: %d' % (self.normal, self.seasonal, self.seasonal_hardcore)
        return output

class Skill(object):
    """ Diablo 3 Spell """
    def __init__(self, slug, name, icon, tooltip_url, description, simple_description, runes, is_active = False):
    	self.slug = slugs
    	self.name = name
    	self.icon = icon
    	self.tooltip_url = tooltip_url
    	self.description = description
    	self.simple_description = simple_description
    	self.runes = runes
    	self.is_active = is_active

class Rune(object):
    """ Diablo 3 Spell Rune """
	def __init__(self, name, skill_slug,  description, simple_description, tooltip_params):
		self.name = name
		self.slug = slug
		self.description = description
		self.simple_description = simple_description
		self.tooltip_params = tooltip_params

class Item(object):
    """ Diablo 3 Spell Rune """
    def __init__(self, id, name, icon, display_color, tooltip_params, transmog_item = None):
        self.id = id
        self.name = name
        self.icon = icon
        self.display_color = display_color
        self.tooltip_params = tooltip_params
        self.transmog_item = transmog_item

    def Rarity(self):
        """ Get Item Rarity """
        #TODO: Test dat shit
        if display_color.lower() == 'orange':
            return 'Legendary'
        elif display_color.lower() == 'green':
            return 'Set'
        elif display_color.lower() == 'yellow':
            return 'Epic'
        elif display_color.lower() == 'blue':
            return 'Rare'
        elif display_color.lower() == 'white':
            return 'Common'
        elif display_color.lower() == 'grey':
            return 'Junk'
        else:
            return 'UNINDENTIFIED'