"""
Nombre de la función:
obtener_indice(lista, elemento)
Objetivo:
Encontrar el índice de la primera ocurrencia de un elemento en la lista.
Tarea:
Buscar en la lista el elemento recibido y retornar su posición (índice).
Si el elemento no existe en la lista, retornar -1.
"""

def obtener_indice(lista: list, elemento: int)-> int:
    """
    Devuelve el indice de la primera aparicion de un elemento en una lista.

    Parametros:
    lista (list): La lista en la que se buscara el elemento.
    elemento (int): El elemento a buscar en la lista.

    Retorno:
    int: El indice de la primera aparicion del elemento.
    """
    for i in range(len(lista)):
        
        if lista[i] == elemento:
            posicion=i
            return posicion
            


lista1 = [0,1,2,3,4,5,6,7,8,9,10]    
num1=1
print(obtener_indice(lista1,num1))