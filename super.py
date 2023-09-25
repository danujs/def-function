#Accessing parent method into a child class with super()

class Racer:
	def __init__(self, name):
		self.name = name



	def getName(self):
		return self.name 


	def getSkill(self):
		return 'normal'

class ItalianRider(Racer):

	#when we use super(), we don't need to use the self parameter

	def __init__(self, name):        #to make automatic, we create function __init__
		# Racer.__init__(self, name) #to call __init__ Racer from parent then it run well
		super().__init__(name)		 #if the Class name somehow too long, we can use super() to access parent's method
		print('Hello argentina')


	def getSkill(self):
		return 'smoother'


Rider = ItalianRider('Rossi')
print(Rider.getName() + " is " + Rider.getSkill())



# Description
"""Each child class that inherit attributes from parent
it can replace certain attributes from that parent"""
"""we can see that Italian and Spain Rider have their own
attributes, while Malaysian inherit the attributes 'getSkill'
from it parent"""