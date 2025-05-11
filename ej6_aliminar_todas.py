"""
Objetivo:
Eliminar todas las ocurrencias de un elemento en la lista.
Tarea:
Modificar la lista original, removiendo todos los elementos iguales al valor recibido.
No es necesario retornar un valor (solo modificar la lista).

Ejemplo: Si la lista es [4, 8, 4, 4, 10] y se eliminan todas las instancias de 4, la lista resultante será [8, 10].
"""

def eliminar_todos(lista: list, elemento: int):
    """
    Elimina todas las apariciones de un elemento en la lista.

    Parametros:
    lista (list): La lista en la que se eliminaran todas las apariciones del elemento.
    elemento (int): El valor a eliminar completamente de la lista.

    Retorno:
    None: La funcion modifica la lista directamente.
    """
   
    i=0
    
    """Mientras que i sea menor al largo de la lista, el bucle sigue."""
    while i < len(lista):
        """Si el el numero con indice igual a i, es igual a elemento, corta la lista para sacarlo"""

        """En caso de que no lo sea, se le suma 1 al valor de i, y el bucle reinicia"""
        if lista[i] == elemento:
            lista[:]= lista[:i]+lista[i+1:]
        else:
            i+=1


        

lista1=[2,10,9,2,2,4,5,6,3,7,2]
num1=2


eliminar_todos(lista1,num1)
print(lista1)
