
'''
e. Se tiene una lista que contiene mensajes encriptados de varios usuarios. 
Cada mensaje se encierra entre {}, y para indicar que se terminó el área de mensajes de 
un usuario se usa un signo &. Indique cuántos usuarios y cuántos mensajes hay en la lista, 
teniendo en cuenta que todos los mensajes están correctamente formados, es decir comienzan 
con { y terminan con }. Y que es seguro que al menos exista un usuario en la lista.
'''
mensajes_encriptados = '{Que onda???}&{Codeanando a lo loco}{Y vos?}&{Por cocinar y tomar unas birras.}{Una compañera se jugo potque la ayudamos con un codigo}&'

contador_usuarios = -1
contador_mensajes = -1

usuarios = mensajes_encriptados.split('&')
mensajes = mensajes_encriptados.split('}')

for i in usuarios:
	contador_usuarios += 1

for i in mensajes:
	contador_mensajes += 1

print(f'Se enviaron {contador_mensajes} mensajes')
print(f'Participaron {contador_usuarios} de usuarios')