#Agenda de contactos

contactos = {}

# Agregar contacto
def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el número: ")
    contactos[nombre] = telefono
    print("Contacto agregado\n")

# Mostrar contactos
def mostrar_contactos():
    if len(contactos) == 0:
        print("No hay contactos registrados\n")
    else:
        print("Lista de contactos:")
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")
        print()

# Buscar contacto
def buscar_contacto():
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in contactos:
        print(f"Teléfono de {nombre}: {contactos[nombre]}\n")
    else:
        print("Contacto no encontrado\n")

# Eliminar contacto
def eliminar_contacto():
    nombre = input("Ingrese el nombre a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print("Contacto eliminado\n")
    else:
        print("Contacto no existe\n")

# Menú principal
while True:
    print("=== AGENDA DE CONTACTOS ===")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida\n")