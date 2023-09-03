class Racer:
	name = 'Valentino Rossi'


	def getName(self):
		return self.name

# outside of class
# we can create  'object' with related name to the 'class'

rider = Racer()
# print(rider.name) #remove the (#), it already has access to call properties 'name'
print(rider.getName()) # call the function 

#we can try another way, by letting the associated property empty.

class Racers:
	name = ''

	def getName2(self, name):
		self.name = name
		return self.name

#outside of class
riders = Racers()
print(riders.getName2('The doctor 46'))
