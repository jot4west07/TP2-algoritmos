from pila import Stack

pila = Stack ()
pila2 = Stack ()
pila3 = Stack () # Funciona como pila auxiliar para volver a llenar pila 2 
# La lista y la pila tienen el mismo tamaño
# Agregar personajes al episodio V

epiV = ["Luke Skywalker", "Leia Organa", "Palpatine", "Yoda", "Darth Vader", "Canciller", "Clon", "Droide"]

# Agregar personajes al episodio VII
epiVII = ["Luke Skywalker", "Leia Organa", "Finn", "Darth Vader", "Han Solo", "Chewbacca", "Canciller", "R2-D2", "Clon", "Robot"]

# se llena la pila 1
if  len(epiV) > 0:
    for i in range(len(epiV)): # epi V se queda vacia
        auxV = epiV.pop()
        pila.push(auxV) # Quita de auxV y apila en pila 1
        
# se llena la pila 2
if  len(epiVII) > 0:
    for i in range(len(epiVII)): # epi VII se queda vacia
        auxVII = epiVII.pop()
        pila2.push(auxVII)

print("")

if pila.size() > 0:
    for i in range(pila.size()): # Ciclos por el tamaño de pila 1
        # Cima_pila1 queda fija y se compara con todos los datos de pila 2 
        cima_pila1 = pila.pop() # Pila 1 se vacia 
        for j in range(pila2.size()): # Vueltas por el tamaño de pila 2
            cima_pila2 = pila2.pop() # Se vacia la pila 2 y cima_pila2 guarda la cima en cada vuelta
            pila3.push(cima_pila2) # Se llena la pila 3 con pila 2 
            if (cima_pila1 == cima_pila2):
                print("El/los personaje/s que coincide/n es/son:")
                print(cima_pila1)
        if pila2.size() == 0: # Si la pila 2 esta vacia
            for h in range(pila3.size()): # El tamaño de pila 3 es igual a pila 2 porque tiene sus elementos
                cima_pila3 = pila3.pop() # Cima pila 3 toma el primer elemento de pila 3 y vacia pila 3 
                pila2.push(cima_pila3) # Pila 2 se llena con los datos de pila 3 
print("")           
