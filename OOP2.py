"""instance attribute: is a function that will automatically run when 
creating the object class
the behavior similar to a mandatory parameter that we have to fill
before using the class

def __init__
"""
class Racer:
	name  = ''
	speed = ''

	def __init__(self, name, speed):
		self.name = name #self.name refers to global variable in line 9, name refer to parameter in line 12
		self.speed = speed 


	def getName(self): #to get the Name, we don't need to use the parameter 'name' again
		return self.name #we can automatically call the return by getting the value of 'self.name' that we have filled before


	def getSpeed(self):
		return self.speed 

rider = Racer('Rossi','330')	#rider is object, here we need to define the value of each parameter in line 12; 'name', and 'speed'
rider2 = Racer('Dani Pedrosa', '349') # the advantage of using OOP, we can create more different objects from one Class
print(rider.getName() + " have a top speed at " + rider.getSpeed() + " km/hour") # now, we can print
print(rider2.getName() + " have a top speed at " + rider2.getSpeed() + " km/hour")

