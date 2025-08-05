def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x.lower() < pivote.lower()]
    iguales = [x for x in lista if x.lower() == pivote.lower()]
    mayores = [x for x in lista[1:] if x.lower() > pivote.lower()]
    return quick_sort(menores) + iguales + quick_sort(mayores)

cantidad = int(input("¿Cuántos nombres desea ingresar? "))
nombres = [input(f"Ingrese el nombre #{i + 1}: ") for i in range(cantidad)]

nombres_ordenados = quick_sort(nombres)
print("\nLista ordenada alfabéticamente:")
for nombre in nombres_ordenados:
    print(nombre)
