import tkinter as tk

inventario = {}

class ExcepcionProducto(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_nombre_producto(nombre):
    if nombre == "":
        raise ExcepcionProducto("El nombre del producto no puede estar vacío.")
    
def validar_precio_producto(precio):
    if precio <= 0:
        raise ExcepcionProducto("El precio del producto debe ser mayor que cero.")
    
def validar_cantidad_producto(cantidad):
    if cantidad < 0:
        raise ExcepcionProducto("La cantidad del producto debe ser mayor o igual cero.")

def agregar_producto(nombre, precio, cantidad):
    try:
        validar_nombre_producto(nombre)
        validar_precio_producto(precio)
        validar_cantidad_producto(cantidad)

        if nombre in inventario:
            inventario[nombre]["Cantidad"] += cantidad
            inventario[nombre]["Valor_total"] += (precio*cantidad)
        else:
            inventario[nombre] = {
                "Precio": precio,
                "Cantidad": cantidad,
                "Valor_total": (precio * cantidad)
            }

        return (
            f"Producto: {nombre}\n"
            f"Precio Unitario: ${precio:.2f}\n"
            f"Cantidad en Inventario: {inventario[nombre]['Cantidad']}\n"
            f"Valor Total en Inventario: ${inventario[nombre]['Valor_total']:.2f}\n"
        )

    except ExcepcionProducto as e:
        return f"Error: {e}"

def agregar_interfaz():
    nombre = nombre_prodcto.get()
    try:
        precio = float(precio_producto.get())
        cantidad = int(cantidad_entrada.get())
        
        resultado = agregar_producto(nombre, precio, cantidad)
        resultados.insert(tk.END, resultado + "\n")
    
    except ValueError:
        resultados.insert(tk.END, "Error: Por favor ingrese valores correctos para el precio y la cantidad.\n")

root = tk.Tk()
root.title("Gestión de Productos en Tienda")

tk.Label(root, text="Producto:").grid(row=0, column=0, padx=10, pady=5)
nombre_prodcto = tk.Entry(root)
nombre_prodcto.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Precio del Producto:").grid(row=1, column=0, padx=10, pady=5)
precio_producto = tk.Entry(root)
precio_producto.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Cantidad del Producto:").grid(row=2, column=0, padx=10, pady=5)
cantidad_entrada = tk.Entry(root)
cantidad_entrada.grid(row=2, column=1, padx=10, pady=5)

boton_añadir = tk.Button(root, text="Agregar a inventario", command=agregar_interfaz)
boton_añadir.grid(row=3, column=0, columnspan=2, pady=10)

resultados = tk.Text(root, height=8, width=40)
resultados.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
