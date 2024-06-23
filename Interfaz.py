from tkinter import Tk, Label, Entry, Button, Frame, PhotoImage
from tkinter import messagebox
from PIL import Image, ImageTk

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Prestamos")

        self.bg_color = "#7F8C8D"  
        self.label_color = "#1A5276"  
        self.button_color = "#154360"  

        self.root.configure(background=self.bg_color)

        self.frame = Frame(root, bg=self.bg_color)
        self.frame.pack(padx=40, pady=40)

        self.add_image()

        Label(self.frame, text="Usuario:", bg=self.bg_color, fg=self.label_color).grid(row=1, column=0, pady=5, sticky="w")
        self.usuario_entry = Entry(self.frame)
        self.usuario_entry.grid(row=1, column=1, pady=5, padx=10)

        Label(self.frame, text="Número de Identificación:", bg=self.bg_color, fg=self.label_color).grid(row=2, column=0, pady=5, sticky="w")
        self.id_entry = Entry(self.frame)
        self.id_entry.grid(row=2, column=1, pady=5, padx=10)

        Label(self.frame, text="Libro:", bg=self.bg_color, fg=self.label_color).grid(row=3, column=0, pady=5, sticky="w")
        self.libro_entry = Entry(self.frame)
        self.libro_entry.grid(row=3, column=1, pady=5, padx=10)

        Label(self.frame, text="Autor:", bg=self.bg_color, fg=self.label_color).grid(row=4, column=0, pady=5, sticky="w")
        self.autor_entry = Entry(self.frame)
        self.autor_entry.grid(row=4, column=1, pady=5, padx=10)

        Label(self.frame, text="Categoría:", bg=self.bg_color, fg=self.label_color).grid(row=5, column=0, pady=5, sticky="w")
        self.categoria_entry = Entry(self.frame)
        self.categoria_entry.grid(row=5, column=1, pady=5, padx=10)

        Label(self.frame, text="Fecha del Préstamo (dd/mm/yyyy):", bg=self.bg_color, fg=self.label_color).grid(row=6, column=0, pady=5, sticky="w")
        self.fecha_prestamo_entry = Entry(self.frame)
        self.fecha_prestamo_entry.grid(row=6, column=1, pady=5, padx=10)

        Label(self.frame, text="Fecha de Devolución (dd/mm/yyyy):", bg=self.bg_color, fg=self.label_color).grid(row=7, column=0, pady=5, sticky="w")
        self.fecha_devolucion_entry = Entry(self.frame)
        self.fecha_devolucion_entry.grid(row=7, column=1, pady=5, padx=10)

        self.boton_prestamo = Button(self.frame, text="Realizar Préstamo", bg=self.button_color, fg="white", command=self.realizar_prestamo_ejemplo)
        self.boton_prestamo.grid(row=8, columnspan=2, pady=10)

        self.boton_mostrar_registros = Button(self.frame, text="Mostrar Registros", bg=self.button_color, fg="white", command=self.mostrar_registros)
        self.boton_mostrar_registros.grid(row=9, columnspan=2, pady=10)

        self.registros = []

    def add_image(self):
        image = Image.open("imgs/IMAGEN.png")
        image = image.resize((150, 150))
        self.photo = ImageTk.PhotoImage(image)

    
        self.image_label = Label(self.frame, image=self.photo, bg=self.bg_color)
        self.image_label.grid(row=0, columnspan=2, pady=10)

    def realizar_prestamo_ejemplo(self):
        nombre_usuario = self.usuario_entry.get()
        id_usuario = self.id_entry.get()
        nombre_libro = self.libro_entry.get()
        autor_libro = self.autor_entry.get()
        categoria_libro = self.categoria_entry.get()
        fecha_prestamo = self.fecha_prestamo_entry.get()
        fecha_devolucion = self.fecha_devolucion_entry.get()

        registro = {
            "Usuario": nombre_usuario,
            "Número de Identificación": id_usuario,
            "Libro": nombre_libro,
            "Autor": autor_libro,
            "Categoría": categoria_libro,
            "Fecha del Préstamo": fecha_prestamo,
            "Fecha de Devolución": fecha_devolucion
        }

        self.registros.append(registro)

        messagebox.showinfo("Préstamo realizado")

        self.usuario_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.libro_entry.delete(0, 'end')
        self.autor_entry.delete(0, 'end')
        self.categoria_entry.delete(0, 'end')
        self.fecha_prestamo_entry.delete(0, 'end')
        self.fecha_devolucion_entry.delete(0, 'end')

    def mostrar_registros(self):
        registros_texto = ""
        for registro in self.registros:
            registros_texto += f"Usuario: {registro['Usuario']}\n"
            registros_texto += f"Número de Identificación: {registro['Número de Identificación']}\n"
            registros_texto += f"Libro: {registro['Libro']}\n"
            registros_texto += f"Autor: {registro['Autor']}\n"
            registros_texto += f"Categoría: {registro['Categoría']}\n"
            registros_texto += f"Fecha del Préstamo: {registro['Fecha del Préstamo']}\n"
            registros_texto += f"Fecha de Devolución: {registro['Fecha de Devolución']}\n"
            registros_texto += "-"*40 + "\n"

        messagebox.showinfo("Registros de Préstamos", registros_texto)

if __name__ == "__main__":
    root = Tk()
    menu = Menu(root)
    root.mainloop()
