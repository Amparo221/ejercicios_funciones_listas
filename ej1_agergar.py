"""
Objetivo:
Agregar un elemento al final de la lista.
Tarea:
Modificar la lista original, añadiendo elemento como su último elemento.
No es necesario retornar un valor (solo modificar la lista).
"""

def agregar(lista: list, elemento: int):
    """
    Agrega un elemento al final de la lista.

    Parametros:
    lista (list): La lista a la que se agregara el elemento.
    elemento (int): El elemento que se desea agregar a la lista.

    Retorno:
    None: La funcion modifica la lista original en su lugar.
    """
    lista[len(lista):] = [elemento]

lista1=[1,2,3,4,5,6]
num1=7
agregar(lista1,num1)
print(lista1)