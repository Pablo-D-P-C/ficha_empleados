print("Completa el formulario para añadir un nuevo usuario")

while True:
    nombre = input("Nombre: ").upper()
    edad = input("Edad: ")
    localidad = input("Localidad: ").upper()
    provincia = input("Provincia: ").upper()
    salario = input("Salario: ")
    dni = input("DNI: ").upper()
    print("Deceas añadir otro usuario: Si ó No?")
    add = input().lower()

    datos = "{}, {}, {}, {}, {}, {}""\n".format(nombre, edad, localidad, provincia, salario, dni)

    with open("empleados.csv", "a") as empleados_file:
        empleados_file.write(str(datos))

    if add == "si":
        continue
    else:
        print("Saliendo ..........")
        break

