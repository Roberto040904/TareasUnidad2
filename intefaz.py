import tkinter as tk
from tkinter import messagebox

#{} para almcenar inventario de producot
inventario = {}


#excepciones (las 3)
class ProductoException(Exception):
    
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def validar_nombre_producto(nombre):
    if nombre == "":
        raise ProductoException("El nombre del producto no puede estar vacío.")
    
def validar_precio_producto(precio):
    if precio <= 0:
        raise ProductoException("El precio del producto debe ser mayor que cero.")
    
def validar_cantidad_producto(cantidad):
    if cantidad < 0:
        raise ProductoException("La cantidad del producto debe ser mayor que 0.")



#agregar productos (nombre, precio, cantidad)

def agregar_producto(nombre, precio, cantidad):
    try:
        validar_nombre_producto(nombre)
        validar_precio_producto(precio)
        validar_cantidad_producto(cantidad)

        if nombre in inventario:
            inventario[nombre]["Cantidad"] += cantidad
            inventario[nombre]["Valor_total"] += (precio * cantidad)
        else:
            inventario[nombre] = {
                "Precio": precio,
                "Cantidad": cantidad,
                "Valor_total": (precio * cantidad)
            }

        return (
            f"Producto: {nombre}"
            f"\nPrecio Unitario: ${precio:.2f}"
            f"\nCantidad en Inventario: {inventario[nombre]['Cantidad']}"
            f"\nValor Total en Inventario: ${inventario[nombre]['Valor_total']:.2f}"
        )

    except ProductoException as e:
        return f"Error: {e}"

def agregar_interfaz():
    
    nombre = entry_nombre.get()
    try:
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())
        
        resultado = agregar_producto(nombre, precio, cantidad)
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos para el precio y la cantidad.")

###INTERFAZZ
root = tk.Tk()
root.title("Gestion de Produtos en tienda")

#productos
tk.Label(root, text="Producto:").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)


#precio
tk.Label(root, text="Precio del Producto:").grid(row=1, column=0, padx=10, pady=5)
entry_precio = tk.Entry(root)
entry_precio.grid(row=1, column=1, padx=10, pady=5)

#cantidad
tk.Label(root, text="Cantidad del Producto:").grid(row=2, column=0, padx=10, pady=5)
entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=2, column=1, padx=10, pady=5)

#al final para agregar
btn_agregar = tk.Button(root, text="Agregar Producto", command=agregar_interfaz)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
