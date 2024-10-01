from classes import dators
import tkinter as tk
from tkinter import ttk, END

visi_datori = []

root = tk.Tk()
root.title("Datoru Veikals")
root.geometry('1000x500')
root.resizable(True, True)

# frame
frame = ttk.Frame(root)

options = {'padx': 5, 'pady': 5}

# Labels
vards_label = ttk.Label(frame, text='Nosaukums: ')
vards_label.grid(column=0, row=0, sticky='W', **options)

skaits_label = ttk.Label(frame, text='Skaits: ')
skaits_label.grid(column=0, row=1, sticky='W', **options)

tips_label = ttk.Label(frame, text='Detaļas tips: ')
tips_label.grid(column=0, row=2, sticky='W', **options)

cena_label = ttk.Label(frame, text='Cena: ')
cena_label.grid(column=0, row=3, sticky='W', **options)

# entry
vards = tk.StringVar()
vards_entry = ttk.Entry(frame, textvariable=vards)
vards_entry.grid(column=1, row=0, **options)
vards_entry.focus()

skaits = tk.StringVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=1, **options)
skaits_entry.focus()

tips = tk.StringVar()
tips_entry = ttk.Entry(frame, textvariable=tips)
tips_entry.grid(column=1, row=2, **options)
tips_entry.focus()

cena = tk.StringVar()
cena_entry = ttk.Entry(frame, textvariable=cena)
cena_entry.grid(column=1, row=3, **options)
cena_entry.focus()

#jaizlabo viss lejā



#
selected_type = tk.StringVar()
selected_type.set("Vīrietis") #Default

# izvēles iespējas
gender_options = ["Vīrietis", "Sieviete", "Cits"]

# OptionMenu
gender_dropdown = tk.OptionMenu(frame, selected_gender, *gender_options)
gender_dropdown.grid(column=1, row=1, **options)

# cita dzimuma rakstīšanai (sākumā paslēpts)
custom_gender_label = ttk.Label(frame, text="Cits dzimums:")
custom_gender = tk.StringVar()
custom_gender_entry = ttk.Entry(frame, textvariable=custom_gender)

#



#līdz šejienei

#funkcijas
def pievienot_sarakstam():
    print("hello world")

#Buttons
vards_button = ttk.Button(frame, text='Pievienot sarakstam', command=pievienot_sarakstam)
vards_button.grid(column=2, row=0, sticky='W', **options)


#listbox



print("hello wowlrtd")

frame.grid(padx=10, pady=10)

# piešķilt grabažu
root.mainloop()