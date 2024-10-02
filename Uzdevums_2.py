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

skaits = tk.IntVar()
skaits_entry = ttk.Entry(frame, textvariable=skaits)
skaits_entry.grid(column=1, row=1, **options)
skaits_entry.focus()

cena = tk.IntVar()
cena_entry = ttk.Entry(frame, textvariable=cena)
cena_entry.grid(column=1, row=3, **options)
cena_entry.focus()


#dropbox menu
selected_type = tk.StringVar()
selected_type.set("Dators") #Default

# izvēles iespējas
type_options = ["Dators", "Programmatūra"]

# OptionMenu
type_dropdown = tk.OptionMenu(frame, selected_type, *type_options)
type_dropdown.grid(column=1, row=2, **options)


#funkcijas
def pievienot_sarakstam():
    tips = selected_type.get()
    nosaukums = vards.get()
    daudzums = skaits.get()
    Cena = cena.get()
    visi_datori.append(dators(nosaukums, daudzums, tips, Cena))
    nomainit_sarakstu()
    print("asyasukfyagwkfuyagwfui")


# Listbox
listbox = tk.Listbox(frame, height=6, selectmode=tk.EXTENDED)
listbox.grid(column=1, row=4, **options)

# listboxa atjaunināšana
def nomainit_sarakstu():
    listbox.delete(0, END)
    for Dators in visi_datori:
        listbox.insert(END, "{}, {}, {}, {}".format(Dators.name, Dators.count, Dators.type, Dators.price))

#Buttons
vards_button = ttk.Button(frame, text='Pievienot sarakstam', command=pievienot_sarakstam)
vards_button.grid(column=2, row=0, sticky='W', **options)


#listbox





frame.grid(padx=10, pady=10)

# piešķilt grabažu
root.mainloop()