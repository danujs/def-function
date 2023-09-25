#Accessing parent method into a child class with super()

class Racer:
	def __init__(self, name):
		self.name = name


	def getName(self):
		return self.name 


	def getSkill(self):
		return 'normal'

class ItalianRider(Racer):


	def __init__(self, name):        #to make automatic, we create function __init__
		# Racer.__init__(self, name) #to call __init__ Racer from parent then it run well
		super().__init__(name)		 #if the Class name somehow too long, we can use super() to access parent's method
		print('Hello argentina')


	def getSkill(self):
		return 'smoother'


Rider = ItalianRider('Rossi')
print(Rider.getName() + " is " + Rider.getSkill())



# Description
"""when we use super(), we don't need to use the self parameter"""
