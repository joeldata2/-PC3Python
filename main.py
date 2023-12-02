import division
import menu
import os
import Problema_2
import Problema_3
import Problema_5
import Problema_8


def main():
    try:
        while True:
            menu.mostrar_menu()
            opcion = menu.obtener_opcion()

            if opcion == 1:
                try:        
                    radio_ingresado = float(input("Ingresa el radio del círculo a calcular:"))
                    el_circulo = Problema_2.Circulo(radio_ingresado)
                    area_del_circulo = el_circulo.calcular_area()
                    print(f"El área del círculo con radio {el_circulo.radio} es: {area_del_circulo}")
                except ValueError:
                    print("Error: Ingresa números solo números.")

            if opcion == 2:
                    catalogo = Problema_3.Catalogo()
                    # Agregar productos al catálogo
                    producto1 = Problema_3.Producto(codigo=1, nombre="Filtro de aceite", precio=15.99)
                    producto2 = Problema_3.Producto(codigo=2, nombre="Batería para automóvil", precio=89.99)
                    catalogo.agregar_producto(producto1)
                    catalogo.agregar_producto(producto2)
                    # Mostrar el catálogo
                    catalogo.mostrar_catalogo()

            if opcion == 3:
                    mi_producto = Problema_5.Producto(nombre="Producto1", codigo="PERU-0001-2023")
                    # Imprimir la representación literal del objeto
                    print(mi_producto)

            if opcion == 4:
                # Dividir dos números
                try:
                    num1 = float(input("Ingresa el primer número: "))
                    num2 = float(input("Ingresa el segundo número: "))
                    resultado = division.dividir(num1, num2)
                    print(f"Resultado de la división: {resultado}")
                except ValueError:
                    print("Error: Ingresa números válidos.")

            if opcion == 5:
                try:
                    nombre = input("Ingresa el nombre: ")
                    edad = input("Ingresa la edad: ")
                    genero = input("Ingresa el género: ")
                    edad = int(edad)
                    persona = Problema_8.Persona(nombre, edad, genero)
                    print("\nDatos de la persona:")
                    print(persona)
                except ValueError:
                    print("Error: La edad debe ser un número entero.")

            elif opcion == 6:
                print(f"Directorio de trabajo: {os.getcwd()}")
                print("Saliendo del programa.")
                break

            else:
                print("Opción no válida. Inténtalo de nuevo.")

    except Exception as e:
        print(f"Error inesperado: {e}")

    finally:
        print("Proceso terminado.")

if __name__ == '__main__':
    main()

