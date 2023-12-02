class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def identificar_pais_lote(self):
        # Dividir el código en partes usando '-'
        partes = self.codigo.split('-')
        
        # Verificar si el código tiene la estructura correcta
        if len(partes) == 3:
            pais = partes[0]
            lote = partes[1]
            año = partes[2]
            return f"País: {pais}, Número de Lote: {lote}, Año: {año}"
        else:
            return "Código no válido"

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}, {self.identificar_pais_lote()}"
