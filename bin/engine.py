#!/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
sys.path.append('.')

from random import randint
import time
import math
from gothonmap import map


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Engine():
	"""
	
	"""

	def __init__(self, scene_map, hero):
        
		self.scene_map = scene_map
		self.hero = hero

	def play(self):
        
		current_scene = self.scene_map.opening_scene()

		session = 0
		while True:
			session += 1
			
			#print type(current_scene).__name__
			if type(current_scene).__name__ == 'Death' or type(current_scene).__name__ == 'Win':
				print u"--- %s %s ---\n" % (map.epilogue_[language], session)
			else:
				print u"--- %s %s ---\n" % (map.chapter_[language], session)
			
			next_scene_name = current_scene.enter(self.hero)

			current_scene = self.scene_map.next_scene(next_scene_name)


class Scene(object):
	"""
	
	"""
	
	def enter(self):
		
		print "This class is for creating subclasses or instances. Subclass it and implement enter()."
		exit(1)


class Death(Scene):
    """

    """

    quips = map.quips_

    def enter(self, hero):

        # testing the gadget
        #for i in range(10):
        #	death_random = randint(1, 3) - 1
        #	print death_random
        #	print map.quips_[language][death_random] % (hero.name)
        death_random = randint(1, 3) - 1
        print map.quips_[language][death_random].decode('utf-8') % (hero.name)
        raw_input(map.continue_[language])
        exit(1)


class LowerDeckCursive(Scene):
    """
       
    """

    def enter(self, hero):

        print map.lower_deck_cursive_[language].decode('utf-8') % (hero.name)

        action = raw_input("[*]> ").lower()

        if action == "a":
            clear()
            print map.lower_deck_cursive_a_[language].decode('utf-8')
            raw_input(map.continue_[language])
            clear()
            return 'death'

        elif action == "b":
            clear()
            print map.lower_deck_cursive_b_[language].decode('utf-8')
            raw_input(map.continue_[language])
            clear()
            return 'death'

        elif action == "c":
            clear()
            print map.lower_deck_cursive_c_[language].decode('utf-8')
            raw_input(map.continue_[language])
            clear()
            return 'armory'

        else:
            clear()
            print map.lower_deck_cursive_else_[language].decode('utf-8')
            time.sleep(4)
            clear()
            return 'lower_deck_cursive'


class Armory(Scene):
	"""
	
	"""
    
	def enter(self, hero):
    
		print map.armory_[language].decode('utf-8')
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))

		print u"\n(Code: " + code + ")\n" # to be deleted

		guesses = 0

		while guesses < 5:
			guess = raw_input("[###]> ")
			##guess = code
			if guess == code:
				break
			clear()
			print u"BZZZZ!...\n"
			guesses += 1
			if guesses == 2:
				clear()
				print map.armory_hunch_[language].decode('utf-8') + "\'" + str(code[0:2]) + "#\'.\n"
			if guesses == 4:
				clear()
				print map.armory_tip_[language].decode('utf-8') + "\'" + str(code) + "\'.\n"

		if guess == code:
			clear()
			print map.armory_code_[language].decode('utf-8')
			raw_input(map.continue_[language])
			clear()
			return 'the_bridge'
		else:
			clear()
			print map.armory_else_[language].decode('utf-8')
			raw_input(map.continue_[language])
			clear()
			return 'death'


class TheBridge(Scene):
	"""
	
	"""
	
	def enter(self, hero):
        
		print map.the_bridge_[language].decode('utf-8')

		action = raw_input("[*]> ").lower()
		if action == "a":
			clear()
			print map.the_bridge_throw_[language].decode('utf-8')
			raw_input(map.continue_[language])
			clear()
			return 'death'

		elif action == "b":
			clear()
			print map.the_bridge_slowly_[language].decode('utf-8')
			raw_input(map.continue_[language])
			clear()
			return 'escape_pod'
		else:
			clear()
			print map.the_bridge_else_[language].decode('utf-8')
			time.sleep(4)
			clear()
			return "the_bridge"
			
			
class EscapePod(Scene):
	"""
	
	"""
	
	def enter(self, hero):
        
		print map.escape_pod_[language].decode('utf-8')

		good_pod = randint(1,5)
		print "\n([#]> " + str(good_pod) +")\n" # to be deleted

		guess = raw_input("[#]> ")

		if int(guess) != good_pod:
			clear()
			print map.escape_pod_not_[language].decode('utf-8') % (guess)
			raw_input(map.continue_[language])
			clear()
			return 'death'
		else:
			clear()
			print map.escape_pod_else_[language].decode('utf-8') % (guess)
			raw_input(map.continue_[language])
			clear()
			return 'final_fight'


class Win(Scene):
	"""
	
	"""

        def enter(self, hero):

            print map.win_[language].decode('utf-8') % (hero.name)
            raw_input(map.continue_[language])
            exit(0)


class Final(Scene):
	"""
	
	"""
	
	def enter(self, hero):

		monster = Monster("Gromble") # initialize a monster

		print map.final_fight_[language].decode('utf-8') % (hero.name, monster.name)
		raw_input(map.continue_[language])
		clear()

		a_combat = Combat()

		next_stage = a_combat.combat(hero, monster)
		return next_stage


class Combat():
	"""
	
	"""
	
	def combat(self, hero, monster):

		round = 1
		# stats monster is stronger, hero recovers faster
		print map.stats_[language].decode('utf-8') % (monster.power, hero.name, hero.power, hero.rate, monster.rate)
		raw_input(map.continue_[language])
		clear()
		
		while True:
			print '='*50
			print '    Round %d' % (round)
			print '='*50
			print map.hp_hero_[language].decode('utf-8') % (hero.name, hero.hp)
			print map.hp_monster_[language].decode('utf-8') % (monster.name, monster.hp)
			print map.what_[language].decode('utf-8') % (hero.name)

			print map.what_attack_[language].decode('utf-8')
			print map.what_defend_[language].decode('utf-8')

			try:
				action = int(raw_input('[#]> '))
				clear()
			except ValueError:
				clear()
				print map.what_except_[language].decode('utf-8') % (hero.name)
				time.sleep(3)
				clear()
				continue


				special = randint(1, 5)
				if special == 1:
					hero.special_attack(monster)
				elif special == 2:
					hero.devastating_attack(monster)
				else:
					hero.attack(monster)
			
			monster_action = randint(1, 5)
			if action == 1:
				if monster_action != 5:
					special = randint(1, 5)
					if special == 1:
						hero.special_attack(monster)
					elif special == 2:
						hero.devastating_attack(monster)
					else:
						hero.attack(monster)
					monster.attack(hero)
				else:
					special = randint(1, 5)
					if special == 1:
						hero.special_attack(monster)
					elif special == 2:
						hero.devastating_attack(monster)
					else:
						hero.attack(monster)
					monster.defend()
			elif action == 2:
				if monster_action != 5:
					hero.defend()
					monster.attack(hero)
				else:
					hero.defend()
					monster.defend()
			else:
				print map.what_no_[language].decode('utf-8')

			# resolve... then
			# whether win or die
			if hero.hp <= 0:
				print map.hero_hp_[language].decode('utf-8')
				raw_input(map.continue_[language])
				clear()
				return 'death'
								
			if monster.hp <= 0:
				print map.monster_hp_[language].decode('utf-8')
				raw_input(map.continue_[language])
				clear()
				return 'win'

			hero.rest()
			monster.rest()

			round += 1

			raw_input(map.continue_[language])			
			clear()

class Species(): # class for species
	"""
	
	"""
	
	defending = 0

	def __init__(self, name):
		
		self.name = name

	def attack(self, target): # attacking state
        
		percent = 0
		if target.defending == 1:
			percent = float(self.power) / 10.0 + randint(0, 10)
			target.hp = math.floor(target.hp - percent)
			print map.attack_[language].decode('utf-8') % (self.name, target.name, target.name, percent)
			time.sleep(1)
		else:
			percent = float(self.power) / 5.0 + randint(0, 10)
			target.hp = math.floor(target.hp - percent)
			print map.attack_[language].decode('utf-8') % (self.name, target.name, target.name, percent)
			time.sleep(1)

	def special_attack(self, target): # special attacking state
        
		percent = 0
		percent = float(self.power) / 1.0 + randint(0, 10)
		target.hp = math.floor(target.hp - percent)
		print map.special_attack_[language].decode('utf-8') % (self.name, target.name, target.name, percent)
		time.sleep(1)

	def devastating_attack(self, target): # special attacking state
        
		percent = 0
		percent = float(self.power) * 2.0 + randint(0, 10)
		target.hp = math.floor(target.hp - percent)
		print map.devastating_attack_[language].decode('utf-8') % (self.name, target.name, percent)
		time.sleep(1)

	def defend(self): # defensive state
        
		self.defending = 1
		print map.defend_[language].decode('utf-8') % (self.name)
		time.sleep(1)

	def rest(self): # recover a bit after each round

		if self.defending == 1:
			percent = self.rate * 10 + randint(0, 10)
		else:
			percent = self.rate * 2 + randint(0, 10)

		self.hp += percent
		print map.rest_[language].decode('utf-8') % (self.name, percent)
		self.defending = 0


class Hero(Species): # for hero
	"""
	
	"""
	
	hp = 125 # life
	power = 200 # attacks
	rate = 3 # recovery


class Monster(Species): # for monster
	"""
	
	"""
	
	hp = 200
	power = 350
	rate = 1


class Map():
	"""
	
	"""
    
	scenes = {
		'lower_deck_cursive': LowerDeckCursive(),
		'armory': Armory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'final_fight': Final(),
		'win': Win()
}

	def __init__(self, start_scene):

		self.start_scene = start_scene

	def next_scene(self, scene_name):

		return Map.scenes.get(scene_name)

	def opening_scene(self):

		return self.next_scene(self.start_scene)


def Lang():
    
    print map.language_
    while True:
        lang = raw_input(str("[e]/[f] >")).lower()
        if lang == 'e':
            language = 0
            return language
        elif lang == 'f':
            language = 1
            return language
        else:
            pass


# code begins executing here
#clear()
clear()
language = Lang()
clear()
#clear()

# Map('lower_deck_cursive') returns LowerDeckCursive()
# into a_map
# a_map is used below
a_map = Map('lower_deck_cursive') # starting room: 'lower_deck_cursive' or 'final_fight'

# print language selection
print map.hero_[language]

# print hero name selection
while True:
	hero_name = raw_input(str("> "))
	if hero_name != "":
		break
clear()

# apply the name
a_hero = Hero(hero_name)

# apply the first room (a_map)
# start the game
a_game = Engine(a_map, a_hero)

# launch the game
a_game.play()
