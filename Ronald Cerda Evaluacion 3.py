import random
import csv

class ConsumoCafe:
    def __init__(self, id_consumo, jugador, edad, equipo, viernes, sabado, domingo):
        self.id_consumo = id_consumo
        self.jugador = jugador
        self.edad = edad
        self.equipo = equipo
        self.viernes = viernes
        self.sabado = sabado
        self.domingo = domingo

    def imprimir_hoja_consumo(self):
        print(f"ID consumo\tJugador\t\tEdad\tEquipo\t\tViernes\tSábado\tDomingo")
        print(f"{self.id_consumo}\t{self.jugador}\t{self.edad}\t{self.equipo}\t{self.viernes}\t{self.sabado}\t{self.domingo}")

lista_consumo = []

def main():
    while True:
        print("\nMenu:")
        print("1. Registrar consumo")
        print("2. Listar todos los consumos")
        print("3. Imprimir hoja de consumo")
        print("4. Buscar consumo por ID")
        print("5. Salir del programa")
        opcion = int(input("Elige la opción que deseas: "))

        if opcion == 1:
            jugador = input("Ingrese su Nombre: ")
            while not jugador.isalpha():
                print("Debe ingresar solo letras para el nombre.")
                jugador = input("Ingrese su Nombre: ")

            edad = int(input("Ingrese su edad: "))
            while edad <= 0:
                print("La edad debe ser un valor numérico mayor a 0.")
                edad = int(input("Ingrese su edad: "))

            equipos = {
                1: "Los Genios de la garrafa",
                2: "Los Compiladores Despiertos",
                3: "Código Borracho",
                4: "Los programadores perezosos",
                5: "Ctrl+Alt+Derrota"
            }
            print("Seleccione su equipo:")
            for key, value in equipos.items():
                print(f"{key}. {value}")

            while True:
                equipo = int(input("Ingrese el número de su equipo (1-5): "))
                if equipo in equipos:
                    equipo = equipos[equipo]
                    print("Equipo registrado correctamente.")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")

            viernes = int(input("Ingrese su consumo de café el día viernes: "))
            sabado = int(input("Ingrese su consumo de café el día sábado: "))
            domingo = int(input("Ingrese su consumo de café el día domingo: "))

            total_dias = viernes + sabado + domingo
            if total_dias >= 3:
                id_consumo = random.randint(1000, 9999)
                consumo = ConsumoCafe(id_consumo, jugador, edad, equipo, viernes, sabado, domingo)
                lista_consumo.append(consumo)
                print("Consumo registrado correctamente.")
            else:
                print("El consumo total debe ser mayor o igual a 3.")

        elif opcion == 2:
            if not lista_consumo:
                print("No hay consumos registrados.")
            else:
                print("Listando todos los consumos:")
                for consumo in lista_consumo:
                    consumo.imprimir_hoja_consumo()

        elif opcion == 3:
            if not lista_consumo:
                print("No hay consumos registrados.")
            else:
                id_consumo = int(input("Ingrese el ID del consumo a imprimir: "))
                encontrado = False
                for consumo in lista_consumo:
                    if consumo.id_consumo == id_consumo:
                        consumo.imprimir_hoja_consumo()
                        encontrado = True
                        break
                if not encontrado:
                    print("No se encontró ningún consumo con ese ID.")

        elif opcion == 4:
            if not lista_consumo:
                print("No hay consumos registrados.")
            else:
                id_consumo = int(input("Ingrese el ID del consumo a buscar: "))
                encontrado = False
                for consumo in lista_consumo:
                    if consumo.id_consumo == id_consumo:
                        consumo.imprimir_hoja_consumo()
                        encontrado = True
                        break
                if not encontrado:
                    print("No se encontró ningún consumo con ese ID.")

        elif opcion == 5:
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, elija una opción del 1 al 5.")

if __name__ == "__main__":
    main()
