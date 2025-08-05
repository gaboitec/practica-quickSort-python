def quick_sort_dict(diccionario):
    if len(diccionario) <= 1:
        return diccionario
    items = list(diccionario.items())
    pivote = items[0][1]

    menores = {k: v for k, v in items[1:] if v.lower() < pivote.lower()}
    iguales = {k: v for k, v in items if v.lower() == pivote.lower()}
    mayores = {k: v for k, v in items[1:] if v.lower() > pivote.lower()}

    return {**quick_sort_dict(menores), **iguales, **quick_sort_dict(mayores)}

cantidad = int(input("¿Cuántas personas desea ingresar? "))
personas = {}

for i in range(cantidad):
    id_estudiante = input(f"Ingrese el ID de la persona #{i + 1}: ")
    nombre_estudiante = input("Ingrese el nombre de la persona: ")
    personas[id_estudiante] = nombre_estudiante

personas_ordenadas = quick_sort_dict(personas)
print("\nEstudiantes ordenados alfabéticamente por nombre:")
for id, nombre in personas_ordenadas.items():
    print(f"{nombre} (ID: {id})")

