"""
Objetivo:
Eliminar el último elemento de la lista y retornarlo.
Tarea:
Modificar la lista original, removiendo su último elemento.
Retornar el elemento eliminado.
Ejemplo: Si la lista es ["a", "b", "c"], al llamar a eliminar(), se retorna "c" y la lista queda ["a", "b"
].
"""

def agregar(lista: list)-> list:
    """
    Elimina el ultimo elemento de la lista y lo devuelve como un valor.

    Parametros:
    lista (list): La lista de la cual se eliminara el ultimo elemento.

    Retorno:
    int: El ultimo elemento eliminado de la lista.
    list: La lista sin el elemento eliminado.
    """


    """Muestra el ultimo elemento de la lista."""
    ultimo = lista[-1]
    """Convierte a la lista entera lista[:] en la lista menos el ultimo elemento: lista[:-1]"""
    lista[:] = lista[:-1]
    
    
    return ultimo



lista1=[1,2,3,4,5,6]


print(agregar(lista1))
print(lista1)













