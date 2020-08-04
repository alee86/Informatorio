'''
Caso 5 OOP

Crear una clase Tiempo, con atributos hora, minuto y segundo, que pueda ser instanciada indicando: 
los tres atributos, sólo la hora y minuto,o sólo la hora. Crear además los métodos necesarios para 
modificar la hora en cualquier momento de forma manual. Mantenga la integridad de los datos en todo 
momento definiendo de tipo “private”. Crear  una  clase prueba_tiempo que  prueba  una  hora  concreta  
y  la  modifique  a  su  gusto  mostrándola  por pantalla.
'''


class Tiempo:
	def __init__(self, hora,minutos=0, segundos=0):
		self.__hora = hora #el __ simula que es privado.
		self.__minutos = minutos
		self.__segundos = segundos

	def getHora(self):
		return(self.__hora)
	def setHora(self,hora):
		self.__hora = hora

		