# Definir el espacio de memoria
espacios_memoria = [1000, 1500, 800, 2000, 600, 1200, 1000, 1800, 700, 1600, 3001]

# Leer los archivos a guardar e identificar sus pesos
archivos = [
    {"nombre": "hola_mundo.py", "tamano": 500},
    {"nombre": "lista_de_compras.txt", "tamano": 950},
    {"nombre": "resumen.docx", "tamano": 1200},
    {"nombre": "persona.h", "tamano": 350},
    {"nombre": "reporte.xlsx", "tamano": 2000}
]


# Algoritmo de Primer ajuste
def primer_ajuste(archivos):
    for archivo in archivos:
        for i in range(len(espacios_memoria)):
            if espacios_memoria[i] >= archivo["tamano"]:
                print(f"Archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb - Bloque asignado: {i}")
                espacios_memoria[i] -= archivo["tamano"]
                break
        else:
            print(f"No hay espacio suficiente para el archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb")


# Algoritmo de Mejor ajuste
def mejor_ajuste(archivos):
    for archivo in archivos:
        mejores_espacios = [i for i in range(len(espacios_memoria)) if espacios_memoria[i] >= archivo["tamano"]]
        if mejores_espacios:
            mejor_espacio = min(mejores_espacios, key=lambda x: espacios_memoria[x])
            print(f"Archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb - Bloque asignado: {mejor_espacio}")
            espacios_memoria[mejor_espacio] -= archivo["tamano"]
        else:
            print(f"No hay espacio suficiente para el archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb")


'''
# Algoritmo de Peor ajuste
def peor_ajuste(archivos):
    for archivo in archivos:
        peor_espacio = max(range(len(espacios_memoria)), key=lambda x: espacios_memoria[x])
        if espacios_memoria[peor_espacio] >= archivo["tamano"]:
            print(f"Archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb - Bloque asignado: {peor_espacio}")
            espacios_memoria[peor_espacio] -= archivo["tamano"]
        else:
            print(f"No hay espacio suficiente para el archivo: {archivo['nombre']} - Tamaño: {archivo['tamano']}kb")
            # Si no hay suficiente espacio para un archivo, detener el algoritmo para ese archivo
            break
'''


def peor_ajuste(espacios_memoria, archivos):
    # Ordenar los espacios de memoria de mayor a menor
    espacios_memoria.sort(reverse=True)

    for archivo in archivos:
        tamano_archivo = archivo["tamano"]
        espacio_asignado = None

        # Encontrar el espacio más grande disponible para el archivo
        for espacio in espacios_memoria:
            if espacio >= tamano_archivo:
                espacio_asignado = espacio
                espacios_memoria.remove(espacio)
                break

        # Si no hay suficiente espacio para el archivo, imprimir un mensaje de error
        if espacio_asignado is None:
            print(f"No hay suficiente espacio para el archivo {archivo['nombre']} de tamaño {tamano_archivo} KB.")
        else:
            print(
                f"El archivo {archivo['nombre']} de tamaño {tamano_archivo} KB fue asignado al espacio {espacio_asignado} KB.")


# Llamar a la función
# peor_ajuste_memoria(espacios_memoria, archivos)

# Algoritmo de Siguiente ajuste
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


# Función principal
def main():
    while True:
        print("\nSeleccione el algoritmo de administración de memoria:")
        print("1. Primer ajuste")
        print("2. Mejor ajuste")
        print("3. Peor ajuste")
        print("4. Siguiente ajuste")
        print("5. Salir")
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
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    main()

'''
Aquí tienes una breve descripción de lo que hace cada algoritmo de administración de memoria 
implementado en el programa:

    Primer Ajuste:
        Descripción: El algoritmo de primer ajuste asigna el primer bloque de memoria disponible 
        que sea lo suficientemente grande para almacenar el archivo. Comienza a buscar desde el 
        principio de la memoria.
        Características: Es rápido y fácil de implementar, 
        pero puede llevar a una fragmentación de memoria.

    Mejor Ajuste:
        Descripción: El algoritmo de mejor ajuste busca el bloque de memoria que sea lo más pequeño 
        posible y aún así sea lo suficientemente grande para almacenar el archivo. 
        Busca en toda la memoria para encontrar el bloque más adecuado.
        Características: Reduce la fragmentación, pero puede ser más lento ya que 
        implica comparar tamaños de bloques.

    Peor Ajuste:
        Descripción: El algoritmo de peor ajuste asigna el bloque de memoria más grande 
        disponible para almacenar el archivo. 
        Busca en toda la memoria para encontrar el bloque más grande.
        Características: Puede llevar a una mayor fragmentación, pero garantiza que los archivos 
        grandes se asignen a bloques grandes.

    Siguiente Ajuste:
        Descripción: El algoritmo de siguiente ajuste comienza la búsqueda desde el último lugar donde 
        se asignó un archivo en memoria. Busca el siguiente bloque disponible desde esa posición.
        Características: Intenta reducir el tiempo de búsqueda al recordar la última 
        posición asignada, pero aún puede llevar a cierta fragmentación.

Cada algoritmo tiene sus ventajas y desventajas en términos de eficiencia y fragmentación de memoria.
La elección del algoritmo depende del contexto específico y de los requisitos del sistema 
en el que se va a implementar.

'''
