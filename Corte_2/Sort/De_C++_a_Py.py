# FUNCIONES DE ENTRADA 

def pedir_entero_positivo(mensaje):
    """Pide un entero positivo, sin permitir letras, símbolos o negativos."""
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            valor = int(valor)
            if valor > 0:
                return valor
        print("1Entrada inválida. Debe ser un número entero mayor que 0.")


def pedir_entero(mensaje):
    """Pide cualquier entero (negativos, cero y positivos permitidos)."""
    while True:
        valor = input(mensaje)
        if valor.lstrip("-").isdigit():
            return int(valor)
        print("Entrada inválida. Solo se permiten números enteros.")


def pedir_lista_enteros(n):
    """Pide n enteros (negativos, cero y positivos permitidos)."""
    arr = []
    print(f"\nIngrese {n} números enteros (negativos y cero permitidos):")

    while len(arr) < n:
        x = pedir_entero(f"Elemento {len(arr) + 1}: ")
        arr.append(x)

    return arr


#  BUBBLE SORT 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


#  INSERTION SORT 
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


#  MERGE SORT 

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l : l + n1]
    R = arr[m + 1 : m + 1 + n2]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


#  QUICK SORT 

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


#  SELECTION SORT 

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


#  PROGRAMA PRINCIPAL 

def main():
    while True:
        print("""
_____________________________
    MENÚ DE ORDENAMIENTO
_____________________________
1. Bubble Sort
2. Insertion Sort
3. Merge Sort
4. Quick Sort
5. Selection Sort
6. Salir
""")

        opcion = pedir_entero("Seleccione una opción (1-6): ")

        if opcion == 6:
            print("\n Saliendo")
            break

        if opcion not in [1, 2, 3, 4, 5]:
            print(" Opción no válida.\n")
            continue

        n = pedir_entero_positivo("\nIngrese el tamaño del arreglo: ")
        arr = pedir_lista_enteros(n)

        print("\nArreglo original:", arr)

        if opcion == 1:
            bubble_sort(arr)
        elif opcion == 2:
            insertion_sort(arr)
        elif opcion == 3:
            merge_sort(arr, 0, n - 1)
        elif opcion == 4:
            quick_sort(arr, 0, n - 1)
        elif opcion == 5:
            selection_sort(arr)

        print("\n Arreglo ordenado:", arr, "\n")


main()
