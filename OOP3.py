# inheritance class of child from parent class
class Racer:
	def __init__(self, name, speed):
		self.name = name
		self.speed = speed

	def getName(self):
		return self.name 

	def getSpeed(self):
		return self.speed 

# Let's add new class
class ItalianRider(Racer):
	def setBikeNumber(self, BikeNumber):
		self.BikeNumber = BikeNumber
		return self.BikeNumber


class SpainRider(Racer):
	def setBikeNumber(self, BikeNumber):
		self.BikeNumber = BikeNumber
		return self.BikeNumber

racer = ItalianRider('Rossi', '330')
racer2 = SpainRider('Pedrosa', '350')
print(racer.getName() + " and his bike number is " + racer.setBikeNumber('46'))
print(racer2.getName() + " and his bike number is " + racer2.setBikeNumber('26'))
# rider = Racer('Rossi', '330')
# rider2 = Racer('Pedrosa', '360')

# print(rider.getName() + " has a top speed at " + rider.getSpeed())
# print(rider2.getName() + " has a top speed at " + rider2.getSpeed())

