"""
Objetivo:
Eliminar la primera ocurrencia de un elemento en la lista y retornarlo.
Tarea:
Buscar la primera aparición de elemento en la lista, eliminarla y retornar el elemento eliminado.
Si el elemento no existe, retornar None y dejar la lista sin cambios.
Ejemplo: Si la lista es [5, 3, 5, 7] y se elimina 5, la lista queda [3, 5, 7] y se retorna 5.
"""

def eliminar_primer_instancia(lista: list, elemento: int)-> int:
    """
    Elimina la primera aparicion de un elemento en la lista y lo devuelve.

    Parametros:
    lista (list): La lista en la que se buscara y eliminara el elemento.
    elemento (int): El valor a buscar y eliminar.

    Retorno:
    int: El elemento eliminado si se encontro. Si no, devuelve None.
    """

    """Recorre la lista basado en su largo"""
    for i in range(len(lista)):
        """En cada indice, verifica si es igual a elemento"""
        if lista[i] == elemento:
            """Si lo es, Guarda ese numero en eliminado"""
            eliminado = lista[i]
            """Corta la lista antes y despues del elemento, y la une, para deshaserce de este"""
            lista[:]= lista[:i]+lista[i+1:]
            
            return eliminado
    return None


lista1=[10,9,3,4,5,6,3,7]
num1=3

print(eliminar_primer_instancia(lista1,num1))
print(lista1)

