"""Objetivo:
Eliminar todos los elementos de la lista, dejándola vacía.
Tarea:
Modificar la lista original, removiendo todos sus elementos.
No es necesario retornar un valor (solo modificar la lista).
Ejemplo: Si la lista es [1, 2, 3], al llamar a vaciar_lista(), la lista quedará [].
"""

def vaciar_lista(lista: list)-> list:
    """
    Vacia la lista, eliminando todos sus elementos.

    Parametros:
    lista (list): La lista que sera vaciada.

    Retorno:
    list: La lista vaciada.
    """
    lista[:] = []
    return lista


lista1=[1,2,3,4,5,6]

print(vaciar_lista(lista1))



