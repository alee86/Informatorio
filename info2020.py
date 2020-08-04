

class Instrumento:
	def __init__ (self, precio):
		self.precio = precio
	def tocar(self):
		print ( "Estamos tocando música" )
	def getPrecio(self):
		print ( "El precio de este instrumento es: $" , self.precio )

	def __str__(self):
		return f'soy un instrumento'
	
class Bateria(Instrumento):
	pass

class Guitarra(Instrumento):
	pass




G = Guitarra(123)

print(G)