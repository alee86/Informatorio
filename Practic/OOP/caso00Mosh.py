'''
Practica del video de Mosh



class Persona:
	def __init__(self, name): #constructor
		self.name = name

	def hablar(self): #metodo
		print(f'Hola, soy {self.name}')


ale = Persona('Aeljandro Eguiazabal')
ale.hablar()

ceci = Persona('Ceci Guinea')
ceci.hablar()


--------------------

class Mammal:
	def walk(self):
			print('caminandoTE')



class Dog(Mammal):
	def bark(self):
		print('ladrido!!')


class Cat(Mammal):
	pass


dog1 = Dog()
dog1.walk()

#DRY: Don't Repeat Yourself (¡No Te Repitas!)
'''

import random


class Dice:
	def roll(self):
		first = random.randint(1,6)
		second = random.randint(1,6)
		return [first, second]



dice = Dice()
print(dice.roll())