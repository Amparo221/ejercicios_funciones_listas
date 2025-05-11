"""
Objetivo:
Insertar un elemento en una posición específica de la lista.
Tarea:
Modificar la lista original, colocando elemento en la posición indicada por indice.
Si el índice es mayor al tamaño de la lista, el elemento se agrega al final.
Ejemplo: Si la lista es [10, 20, 30] y se inserta 5 en el índice 1, la lista resultante será [10, 5, 20, 30].
"""

def insertar(lista: list, elemento: int, indice: int):
    """
    Inserta un elemento en una posicion especifica de la lista(o al final de esta si el indice es mator a la longitud de la lista).

    Parametros:
    lista (list): La lista donde se insertara el elemento.
    elemento (int): El valor entero a insertar.
    indice (int): La posicion en la que se desea insertar el elemento.

    Retorno:
    None: La funcion modifica la lista original directamente.
    """
    if indice>len(lista):
       lista[len(lista):] = [elemento]
    else:
        lista[indice:indice] = [elemento]



lista1=[1,2,3,4,5,6,8,9,10]
num1=7
num2=6
insertar(lista1,num1,num2)
print(lista1)