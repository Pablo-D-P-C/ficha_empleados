empleados = "empleados.csv"

with open(empleados) as empleados_file:
    for empleado in empleados_file.readlines():
        nombre, edad, localidad, provincia, salario, dni = empleado.split(",")
        dni = dni.replace("\n", "")
        print(f"{nombre} {edad} {localidad} {provincia} {salario} {dni}")

        datos = "{5}, {4}, {3}, {2}, {1}, {0}""\n".format(nombre, edad, localidad, provincia, salario, dni)

        try:
            with open("empleados_reverso.csv", "x") as empleados_reverso_file:
                empleados_reverso_file.write(str(datos))
        except FileExistsError:
            print("Valores duplicados")