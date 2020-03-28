
# Soldier


class Soldier:
    def __init__(self, health, strength):
    	self.health = health
    	self.strength = strength
    	

    def attack(self):
    	return self.strength


    def receiveDamage(self, damage):
    	self.damage = damage
    	self.health = self.health - self.damage



# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
    	super().__init__(health, strength)
    	self.name = name


    def battleCry(self):
    	return "Odin Owns You All!"


    	
# Saxon


class Saxon(Soldier):
	def __init__(self, health, strength):
		super().__init__(health, strength)
	 
	def receiveDamage(self, damage):
		self.damage = damage
		self.health = self.health - self.damage

		if self.health > 0:
    		#self.health = self.health - self.damage
			return "A Saxon has received {} points of damage".format(self.damage)
		else:
			return "A Saxon has died in combat"



# War
from random import choice

class War:
	def _init__(self, saxonArmy, vikingArmy):
		self.vikingArmy = []
		self.saxonArmy = []


	def addViking(self, Viking):
		self.vikingArmy.append(Viking)

	def addSaxon(self, Saxon):
		self.saxonArmy.append(Saxon)

	def vikingAttack(self):
		s = choice(self.saxonArmy) 
		v = choice(self.vikingArmy)
		s.receiveDamage = v.attack
		self.saxonArmy = [s for s in self.saxonArmy if s.health > 0]


	def saxonAttack(self):
		s = choice(self.saxonArmy) 
		v = choice(self.vikingArmy)
		v.receiveDamage = s.attack
		self.vikingArmy = [v for v in self.vikingArmy if s.health > 0]

	def showStatus(self):
		pass
