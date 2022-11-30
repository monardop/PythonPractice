import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random


bg_colour = "#3d6466"

def clear_widget(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def fetch_db():
    connection = sqlite3.connect("data/recipes.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()
    idx = random.randint(0,len(all_tables)-1)
    #get ingredients
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()
    return table_name, table_records
   
def pre_proces(table_name, table_records): 
    tittle = table_name[:-6]
    #Cada elemento empieza con mayuscula, asi que lo uso para buscar las palabras
    tittle = "".join([char if char.islower() else " " + char for char in tittle])
    ingridients = []
    for i in table_records:
        name = i[1]
        qty = i[2]
        unit = i[3]
        ingridients.append(qty + " " + unit + " of " + name)
    return tittle, ingridients

def load_frame1():
    clear_widget(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False) #Esto evita que lo que esté adentro pise el fondo o lo que sea que agregue al frame.
    #Frame1: Widgets
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")#esta es la manera de importar imagenes al programa
    logo_widget = tk.Label(frame1, image=logo_img,bg= bg_colour)
    logo_widget.image = logo_img #convención, de otra manera puede haber errores raros
    logo_widget.pack()

    tk.Label(
        frame1, 
        text="Click for some random recipe",
        bg=bg_colour,
        fg= "white",
        font=("TkMenuFont", 14)
        ).pack()   

    #button widget
    tk.Button(
        frame1, 
        text="Shuffle", 
        font=("TkHeadingFont", 20),
        bg="#28393a",
        fg="white",cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2() #si no agrego el lamda la función se ejecuta ni bien arranca el programa, y no responde a click. Con lambda se vuelve funcion de evento.
        ).pack(pady=20)

def load_frame2():
    clear_widget(frame1)
    frame2.tkraise()

    table_name, table_records = fetch_db()
    title, ingredients = pre_proces(table_name, table_records)
    logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo_bottom.png")#esta es la manera de importar imagenes al programa
    logo_widget = tk.Label(frame2, image=logo_img,bg= bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Label(
        frame2, 
        text=title,
        bg=bg_colour,
        fg= "white",
        font=("TkHeadingFont", 20)
        ).pack(pady=25)  
    for i in ingredients:
        tk.Label(
            frame2, 
            text=i,
            bg="#28393a",
            fg= "white",
            font=("TkMenuFont", 10)
            ).pack(fill="both")  

    tk.Button(
        frame2, 
        text="Back", 
        font=("TkHeadingFont", 18),
        bg="#28393a",
        fg="white",cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame1() 
        ).pack(pady=20)

# initiallize app
root = tk.Tk()
root.title("Recipe random Picker")
#root.eval("tk::PlaceWindow . center")
"""
x= root.winfo_screenwidth() // 2 #El doble barra redondea hacia abajo
y = int(root.winfo_screenheight() * 0.1) #Ajusto un 10% abajo del borde sup de la pantalla 
root.geometry('500x600+' + str(x) + '+' + str(y)) #ajusta la pantalla con las medidas que puse
Esto genera problemas con la panatalla al momento de reajustar. No sirve y arruina la portabilidad.
"""

#Frame principal
frame1 = tk.Frame(root,width=800, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)
#frame1.grid(row=0, column=0)
#frame2.grid(row=0, column=0)
for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky="nesw")
#sticky nesw es north east south west. Expande todo para llenar la pantalla y que no me queden huecos si algo es mas ancho
load_frame1()



# run app
root.mainloop()