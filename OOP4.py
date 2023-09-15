#Override Parent Function

class Racer:
	def __init__(self, name, speed):
		self.name = name
		self.speed = speed


	def getName(self):
		return self.name 


	def getSpeed(self):
		return self.speed 


	def getSkill(self):
		return 'normal'

class ItalianRider(Racer):
	def getSkill(self):
		return 'smoother'


class SpainRider(Racer):
	def getSkill(self):
		return 'fast' 

class MalaysianRider(Racer):
	pass

Rider = ItalianRider('Rossi', '330')
print(Rider.getName() + " is " + Rider.getSkill())
Rider2 = SpainRider('Pedrosa', '360')
print(Rider2.getName() + " is " + Rider2.getSkill())
Rider3 = MalaysianRider('Sulthan','280')
print(Rider3.getName() + " is " + Rider3.getSkill())


# Description
"""Each child class that inherit attributes from parent
it can replace certain attributes from that parent"""
"""we can see that Italian and Spain Rider have their own
attributes, while Malaysian inherit the attributes 'getSkill'
from it parent"""