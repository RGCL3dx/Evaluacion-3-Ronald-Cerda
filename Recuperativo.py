import re

registro = []  

def certificado(persona):
    print("CERTIFICADO AFILIACION ISAPRE VIDA Y SALUD")
    print("Se otorga el siguiente certificado de afiliacion a:")
    print("Nombre:", persona["Nombre"])
    print("Apellido:", persona["Apellido"])
    print("Rut:", persona["Rut"])
    print("Edad:", persona["Edad"])
    print("Estado Civil:", persona["Estado Civil"])
    print("Afiliado en esta institucion desde", persona["Fecha Afiliacion"])
    print("Se otorga certificado de afiliacion ")
    print("CERTIFICADO AFILIACION ISAPRE VIDA Y SALUD")

def main():
    print("1. Guardar")
    print("2. Buscar")
    print("3. Imprimir")
    print("4. Salir")
    op = int(input("Seleccione una opcion del 1 al 4: "))

    if op == 1:
        rut = input("Ingrese su rut: ")
        if len(rut) != 9:
            print("Debe tener 9 digitos")
            main()
        
        nombre = input("Ingrese su nombre: ")
        while nombre == "":
            print("No debe estar vacio")
            nombre = input("Ingrese su nombre: ")

        apellido = input("Ingrese su apellido: ")
        while apellido == "":
            print("No debe estar vacio")
            apellido = input("Ingrese su apellido: ")

        while True:
            edad = input("Ingrese su edad: ")
            if edad.isdigit() and int(edad) >= 18:
                break
            else:
                print("Debe ser un numero mayor o igual a 18")

        while True:
            estado = input("Ingrese su estado civil (c=casado, s=soltero, v=viudo): ")
            if estado in ['c', 's', 'v']:
                break
            else:
                print("Ingrese una de las opciones validas: c, s, v")

        fecha = input("Ingrese su fecha de afiliacion: ")

        persona = {
            "Rut": rut,
            "Nombre": nombre,
            "Apellido": apellido,
            "Edad": edad,
            "Estado Civil": estado,
            "Fecha Afiliacion": fecha
        }

        registro.append(persona)
        print("Registro guardado correctamente:")
        print(persona)
        main()

    elif op == 2:
        buscar = input("Seleccione la persona a buscar por su estado civil (c/s/v): ")
        if buscar in ['c', 's', 'v']:
            print("Personas con estado civil", buscar)
            for persona in registro:
                if persona["Estado Civil"] == buscar:
                    print(persona)
        else:
            print("Ingrese una de las opciones validas: c, s, v")
        main()

    elif op == 3:
        for persona in registro:
            certificado(persona)
        main()

    elif op == 4:
        print("Hasta luego, gracias por preferir ISAPRE VIDA Y SALUD")
        print("Ronald Cerda, Ingenieria en Informatica")

    else:
        print("Opción invalida. Seleccione una opcion del 1 al 4.")
        main()

main()