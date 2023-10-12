# Definir el espacio de memoria
espacios_memoria = [1000, 1500, 800, 2000, 600, 1200, 1000, 1800, 700, 1600, 3001]


# Leer los archivos desde el archivo "archivos.txt"
def leer_archivos():
    archivos = []
    with open("archivos.txt", "r") as file:
        for line in file:
            nombre, tamano = line.strip().split(", ")
            tamano = int(tamano[:-2])  # Eliminar "kb" del tamaño y convertir a entero
            archivos.append({"nombre": nombre, "tamano": tamano})
    return archivos


###########################################################################################
def agregar_archivo():
    nombre_archivo = input("Nombre del Archivo: ")
    tamano_archivo = input("Tamaño en kb: ")
    ubicacion = input("¿Donde desea añadir el archivo, al Principio o Final? ").lower()
    archivo_nuevo = f"{nombre_archivo}, {tamano_archivo}kb\n"

    with open("archivos.txt", "r+") as file:
        contenido = file.readlines()

        if ubicacion == "principio":
            contenido.insert(0, archivo_nuevo)
        else:
            contenido.append(archivo_nuevo)

        file.seek(0)
        file.writelines(contenido)
        print(f"Archivo '{nombre_archivo}' añadido correctamente al archivo 'archivos.txt' al {ubicacion}.")


## 1. Primer ajuste #######################################################################
# (Algoritmo de Primer ajuste)
def primer_ajuste(archivos):
    for archivo in archivos:
        for i in range(len(espacios_memoria)):
            if espacios_memoria[i] >= archivo["tamano"]:
                print(f"Archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb - Bloque asignado: {i}")
                espacios_memoria[i] -= archivo["tamano"]
                break
        else:
            print(f"No hay espacio suficiente para el archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb")


##  2. Mejor ajuste #########################################################################
# (Algoritmo de Mejor ajuste)
def mejor_ajuste(archivos):
    for archivo in archivos:
        mejores_espacios = [i for i in range(len(espacios_memoria)) if espacios_memoria[i] >= archivo["tamano"]]
        if mejores_espacios:
            mejor_espacio = min(mejores_espacios, key=lambda x: espacios_memoria[x])
            print(f"Archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb - Bloque asignado: {mejor_espacio}")
            espacios_memoria[mejor_espacio] -= archivo["tamano"]
        else:
            print(f"No hay espacio suficiente para el archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb")


## 3. Peor ajuste ############################################################################
# (Algoritmo de Peor ajuste)
def peor_ajuste(espacios_memoria, archivos):
    espacios_memoria.sort(reverse=True)
    for archivo in archivos:
        tamano_archivo = archivo["tamano"]
        espacio_asignado = None
        for espacio in espacios_memoria:
            if espacio >= tamano_archivo:
                espacio_asignado = espacio
                espacios_memoria.remove(espacio)
                break
        if espacio_asignado is None:
            print(f"No hay suficiente espacio para el archivo {archivo['nombre']} de tamaño {tamano_archivo} KB.")
        else:
            print(
                f"El archivo {archivo['nombre']} de tamaño {tamano_archivo} KB fue asignado al espacio {espacio_asignado} KB.")


## 4. Siguiente ajuste ##########################################################################
# (Algoritmo de Siguiente ajuste)
def siguiente_ajuste(archivos):
    ultimo_espacio_usado = 0
    for archivo in archivos:
        for i in range(ultimo_espacio_usado, len(espacios_memoria)):
            if espacios_memoria[i] >= archivo["tamano"]:
                print(f"Archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb - Bloque asignado: {i}")
                espacios_memoria[i] -= archivo["tamano"]
                ultimo_espacio_usado = i
                break
        else:
            print(f"No hay espacio suficiente para el archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb")


## main() ##################################################################################
def main():
    archivos = leer_archivos()
    while True:
        print("\nSeleccione el algoritmo de administración de memoria:")
        print("1. Primer ajuste")
        print("2. Mejor ajuste")
        print("3. Peor ajuste")
        print("4. Siguiente ajuste")
        print("5. Agregar archivo a la memoria")
        print("6. Salir")
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            primer_ajuste(archivos)
        elif opcion == "2":
            mejor_ajuste(archivos)
        elif opcion == "3":
            peor_ajuste(espacios_memoria, archivos)
        elif opcion == "4":
            siguiente_ajuste(archivos)
        elif opcion == "5":
            agregar_archivo()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


####################################################################################
if __name__ == "__main__":
    main()
####################################################################################
####################################################################################
