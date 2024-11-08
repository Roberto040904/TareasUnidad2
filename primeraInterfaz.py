import tkinter as tk
from tkinter import messagebox

import tkinter as tk
 
root = tk.Tk()

  
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        restar = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {restar}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def multiplicacion():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        multiplicacion = num1 * num2
        messagebox.showinfo("Resultado", f"La multiplicacion es: {multiplicacion}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
def division():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        division = num1 / num2
        messagebox.showinfo("Resultado", f"La division es: {division}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
        
    except ZeroDivisionError:
        messagebox.showerror("Error", "Estas dividiendo entre 0.")
        

 
 
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("450x400")
 
label_num1 = tk.Label(ventana, text="Número 1:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack(pady=5)
 
label_num2 = tk.Label(ventana, text="Número 2:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack(pady=5)
 
boton_sumar = tk.Button(ventana, text="Sumar", bg="pink", fg="white", font=("Arial", 12), command=sumar)
boton_sumar.pack(pady=20)

boton_restar = tk.Button(ventana, text="Restar", bg="blue", fg="white", font=("Arial", 12), command=restar)
boton_restar.pack(pady=20)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", bg="green", fg="white", font=("Arial", 12), command=multiplicacion)
boton_multiplicar.pack(pady=20)

boton_division = tk.Button(ventana, text="Division", bg="red", fg="white", font=("Arial", 12), command=division)
boton_division.pack(pady=20)
 
ventana.mainloop()
 
