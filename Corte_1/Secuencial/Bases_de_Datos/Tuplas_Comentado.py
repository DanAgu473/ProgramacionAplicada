# Inicializa una lista llamada 'mi_lista' con seis elementos de tipo string (colores).
mi_lista= ['Rojo', 'Azul', 'Amarillo', 'Verde', 'Violeta', 'Naranja']

# Imprime el contenido completo de la lista.
print(mi_lista)
# Imprime el tipo de la variable 'mi_lista', que será <class 'list'>.
print(type(mi_lista))
# Imprime el elemento en el índice 2 ('Amarillo').
print(mi_lista[2])
# Usa la función len() para obtener e imprimir el número de elementos en la lista.
print("Tamaño Lista", len(mi_lista))
# Imprime un 'slice' (trozo) de la lista, desde el índice 1 (incluido) hasta el 3 (excluido).
print(mi_lista[1:3])
# Imprime un 'slice' desde el inicio de la lista (índice 0) hasta el índice 3 (excluido).
print(mi_lista[:3])


###    Funciones propias de las listas    ###

# Añade el elemento 'Blanco' al final de la lista.
mi_lista.append('Blanco')
print(mi_lista)
# Inserta el elemento 'Negro' en el índice 4 de la lista, desplazando los elementos siguientes.
mi_lista.insert(4,'Negro')
print(mi_lista)
# Extiende la lista añadiendo todos los elementos de la lista ['Marron', 'Gris'] al final.
mi_lista.extend(['Marron','Gris'])
print(mi_lista)

# Retorna e imprime el índice (posición) del primer elemento 'Azul' encontrado.
print(mi_lista.index('Azul'))

# Elimina la primera ocurrencia del elemento 'Marron' de la lista.
mi_lista.remove('Marron')
print(mi_lista)

# Elimina y retorna el elemento ubicado en el índice 8, imprimiéndolo.
print(mi_lista.pop(8))


print("Orden")
# Crea una nueva lista 'mi_lista_ord' con los elementos de 'mi_lista' ordenados alfabéticamente (no modifica la lista original).
mi_lista_ord = sorted(mi_lista)
print(mi_lista_ord)


# Inicializa una nueva lista con números en orden descendente.
mi_listaNum= [10,9,8,7,6,5,4,3,2,1]
print(mi_listaNum)
print("Ordenando Mi lista Numerica")

# Ordena la lista 'mi_listaNum' en su lugar (modificación directa), de menor a mayor.
mi_listaNum.sort()
print(mi_listaNum)

# Ordena la lista 'mi_listaNum' en su lugar, de mayor a menor (descendente) debido al parámetro reverse=True.
mi_listaNum.sort(reverse=True)
print(mi_listaNum)


#    Operadores    #

# Crea una nueva lista 'mi_lista3' repitiendo los elementos de 'mi_lista' tres veces (operador de multiplicación).
mi_lista3 = mi_lista*3
print("Mi lista 3 veces: ",mi_lista3)

# Crea una nueva lista 'mi_listamas' concatenando los elementos de 'mi_lista' consigo misma (operador de suma).
mi_listamas = mi_lista+mi_lista
print("Mi lista + mi lista: ",mi_listamas)


    #Tuplas en Python#
    #Listas que no pueden ser modificadas una vez sean inicializadas


# Convierte la lista 'mi_lista' actual en una tupla (estructura inmutable).
mi_tupla= tuple(mi_lista)
print("Mi tupla: " ,mi_tupla)

# Imprime el primer elemento de la tupla (índice 0).
print(mi_tupla[0])
# Imprime el tercer elemento de la tupla (índice 2).
print(mi_tupla[2])

# Verifica si el string 'Rojo' está presente en la tupla y devuelve un booleano.
print('Rojo' in mi_tupla)

# Cuenta cuántas veces el elemento 'Rojo' aparece en la tupla.
print(mi_tupla.count('Rojo'))

# Genera una tupla que contiene un solo elemento 'Fucsia'.
mi_tupla_unitaria = ('Fucsia')
print(mi_tupla_unitaria)

# Crea una tupla con varios tipos de datos.
mi_tupla = 'Gaspar' , 5, 8, 1999
print(mi_tupla)

# 'Desempaqueta' la tupla, asignando sus valores a las variables en orden.
nombre, dia, mes, año = mi_tupla
print(nombre)
print(dia)
print(mes)
print(año)
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convierte la tupla 'mi_tupla' de nuevo a una lista.
milista_Final =list(mi_tupla)
print(milista_Final)


#    Informacion obtenida de ThinkPython segunda edicion
#    https://www.w3schools.com/python/ref_list_index.asp
#    https://www.freecodecamp.org/espanol/news/funcion-pop-en-python/