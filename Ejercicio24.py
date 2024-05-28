from pila import Stack
pila = Stack ()
pila2 = Stack ()
# Hay 8 personajes
diccionario = {'Spider man':'6','Wolverine':'7',"Hulk":'3', 'Viuda negra':'2', 'Rocket Raccoon':'1','Doctor Strange':'4','Groot':'2', 'Capitan america':'7', 'Thor':'5', 'Iron man':'8', 'Pantera negra':'3', 'Ciclope':'6','Magneto':'6','Deadpool':'5', 'Gamora':'2'}


nombres_con_c = []
nombres_con_d = []
nombres_con_g = []

vuelta = 1
if len(diccionario) > 0: # Se carga la pila en cada posicion con nombre:cantidad de peliculas
    for i in range(len(diccionario)): 
        dato = diccionario.popitem() # Para quitar el elemento de un diccionario se usa popitem() y no pop ()
        pila.push(dato) 

# dato guarda en cada posicion de la pila una tupa del tipo (nomre : cantidad de peliculas)
# para acceder a nombre se usa dato[0] y para acceder a cantida de peliculas se usa dato [1]
# las tuplas son como las listas, se puede acceder a cada elemento a traves de su posicion (desde cero)

for i in range(pila.size()):
    
    dato = pila.pop() # Pila 1 se vacia 
    if dato[0] == 'Rocket Raccoon':
        print("Rocket Raccoon esta en la posicion: ", vuelta)
    elif dato[0] == 'Groot':
        print("Groot esta en la posicion: ", vuelta)
    vuelta = vuelta + 1
    pila2.push(dato)
print("")
for i in range(pila2.size()):
    dato = pila2.pop() # Pila 2 se vacia 
    if dato [1] >='5': # compara 5 como un string porque en el diccionario las values son strings
        print("El siguiente personaje participo en mas de 5 peliculas: ", dato[0])
        print("Participo en esta cantidad de peliculas: ", dato[1])
    pila.push(dato)
print("")
for i in range(pila.size()):
    dato = pila.pop() # pila 1 queda vacia
    if dato[0] == "Viuda negra":
        cant_pelis = dato[1]
        print("Viuda negra participo en esta cantidad de peliculas: ", cant_pelis)
    pila2.push(dato)
print("")
for i in range(pila2.size()):
    dato = pila2.pop() # Vacia la pila 2 
    nombre = dato[0]
    nombre_minusculas = nombre.lower() # lower() pasa a minusculas a todos los nombres, funciona aunque no este marcado
    if nombre_minusculas[0] == 'c': # nombre_minusculas[0] toma la primer letra de cada nombre del personaje
        nombres_con_c.append(nombre) # Agregar a la lista con este metodo y no nombres_con_c = nombre
    elif nombre_minusculas[0] == 'd':
        nombres_con_d.append(nombre) # Agregar a la lista con este metodo y no nombres_con_d = nombre
    elif nombre_minusculas[0] == 'g':
        nombres_con_g.append(nombre) # Agregar a la lista con este metodo y no nombres_con_g = nombre

for i in range(len(nombres_con_c)): # i toma cada posicion, la cual es el nombre del personaje
    print("Los personajes que comienzan su nombre con C son: ", nombres_con_c[i])

for i in range(len(nombres_con_d)):
    print("Los personajes que comienzan su nombre con D son: ", nombres_con_d[i])

for i in range(len(nombres_con_g)):
    print("Los personajes que comienzan su nombre con G son: ", nombres_con_g[i])








