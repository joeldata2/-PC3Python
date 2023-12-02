class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class Catalogo:
    def __init__(self):
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print(f"Producto {producto.nombre} agregado al catálogo.")

    def mostrar_catalogo(self):
        if not self.lista_productos:
            print("El catálogo está vacío.")
        else:
            print("Catálogo de productos:")
            for producto in self.lista_productos:
                print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: {producto.precio}")

