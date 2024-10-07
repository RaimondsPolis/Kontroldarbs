from classes import dators, Detala
import tkinter as tk
from tkinter import ttk, END
from tkinter import *

visi_datori = []

root = tk.Tk()
root.title("Datoru Veikals")
root.geometry('600x500')
root.resizable(True, True)

# frame
frame = ttk.Frame(root)

options = {'padx': 5, 'pady': 5}

# Listbox
listbox = tk.Listbox(frame, height=10, width=50, selectmode=tk.EXTENDED)
listbox.grid(column=1, row=4, **options)

# Labels
vards_label = ttk.Label(frame, text='Nosaukums: ')
vards_label.grid(column=0, row=0, sticky='W', **options)

skaits_label = ttk.Label(frame, text='Skaits: ')
skaits_label.grid(column=0, row=1, sticky='W', **options)

tips_label = ttk.Label(frame, text='Preces tips: ')
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

razotajs_label = ttk.Label(frame, text='Ražotajs:       ')
razotajs = tk.StringVar()
razotajs_entry = ttk.Entry(frame, textvariable=razotajs)



#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#Create the option and Check Button Event
def OptionMenu_CheckButton(event):
    var.get()
    if var.get() == options1[0]:
        razotajs_entry.grid(column=1, row = 3, sticky='W', **options)
        razotajs_label.grid(column=0, row=3, sticky='W', **options) 
        cena_label.grid(column=0, row=4, sticky='W', **options)
        listbox.grid(column=1, row=5, **options)
        cena_entry.grid(column=1, row=4, **options)
        print("asdasd")
    else: #                                            VISS STRĀDĀAAAAAAAAAAAAAAAAAAAAA
        print("qwert")
        razotajs_entry.grid_forget()                # kaut kā negribās turēties pareizajā vietā tam razotajs_entry, visu ķipa izmēģināju, viņ buggo
        razotajs_label.grid_forget()
    pass
#AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

#aj tā pat būs 7 ne?


#Ko es uzzināju pēc apmēram 8 stundām? StringVar nav strings bet gan vērtība kas satur stringu. ja grib no stringvar dabūt string vajag stirngvar.get()
      

#Create the variables
var = StringVar()
var.set("Programmatūra")
options1 = ["Dators/Detaļa","Programmatūra"]
OptionMenu(frame, var, *(options1), command =
OptionMenu_CheckButton).grid(column=1, row= 2, **options)


#funkcijas
def pievienot_sarakstam():
    if var.get() == "Dators/Detaļa":
        
        tips = var.get()
        nosaukums = vards.get()
        daudzums = skaits.get()
        Cena = cena.get()
        Razotajs = razotajs.get()
        visi_datori.append(Detala(nosaukums, Razotajs, daudzums, tips, Cena))
        nomainit_sarakstu()
        print(Razotajs)
    else:    
        tips = var.get()
        nosaukums = vards.get()
        daudzums = skaits.get()
        Cena = cena.get()
        visi_datori.append(dators(nosaukums, daudzums, tips, Cena))
        #result_label.config(text=visi_datori[-1].info())
        nomainit_sarakstu()
        print(Cena)

redzets = 0
# paņemts no nodarbības funkcijas lmao (came in clutch)
def nopirkts():
    jaunais_teksts = ""
    for izveletais in listbox.curselection():
        if isinstance(visi_datori[izveletais].count, int): #isinstance pārbauda vai dotais mainīgais ir vienāds ar izvēlēto datu tipu
            visi_datori[izveletais].count -=1
            if isinstance(visi_datori[izveletais], dators):
                jaunais_teksts += visi_datori[izveletais].info() + "\n"
            else:
                jaunais_teksts +=visi_datori[izveletais].info1()+ "\n"

            global redzets # paldies stackoverflow par šo ideju <3
            redzets += visi_datori[izveletais].price
            print (redzets) #lai parliecinātos ka strādā

            if visi_datori[izveletais].count <=0:
                visi_datori[izveletais].count = "IZPIRKTS/SOLD OUT"
                nomainit_sarakstu()

    result_label.config(text="Nopelnīts: "+ str(redzets)+"$")

    nomainit_sarakstu()



def vardamaina_clicked():
    nameChange = tk.Toplevel(root)
    nameChange.title('Datu rediģēšana')
    nameChange.resizable(False, False)
    window_width = 450
    window_height = 200

    screen_width = nameChange.winfo_screenwidth()
    screen_height = nameChange.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    nameChange.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    # funkcijas
    def jaunaisvards():
        datora_vards = jvards.get()
        datora_skaits = jskaits.get()
        datora_cena = jcena.get()
        Razotajs = jrazotajs.get()
        
        if not datora_vards:
            datora_vards = vards.get()

        if datora_skaits == "":
            datora_skaits = skaits.get()
        else:
            datora_skaits = int(datora_skaits)

        if datora_cena == "":
            datora_cena = cena.get()
        else:
            datora_cena = int(datora_cena)

# NESTRĀDĀ RAŽOTĀJA MAIŅA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        for izveletais in listbox.curselection():
            visi_datori[izveletais].name = datora_vards
            visi_datori[izveletais].count = datora_skaits
            visi_datori[izveletais].price = datora_cena
            visi_datori[izveletais].type = selected_option.get()
            if selected_option.get() == "Dators/Detaļa":
                visi_datori[izveletais].producer = Razotajs
            if not Razotajs:
                Razotajs = razotajs.get()
        nomainit_sarakstu()
        nameChange.destroy()
# NESTRĀDĀ RAŽOTĀJA MAIŅA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


    #labels
    jaunsvards_label = ttk.Label(nameChange, text='Jaunais nosaukums:')
    jaunsvards_label.grid(column=0, row=0, sticky='W', **options)

    jaunaisskaits_label= ttk.Label(nameChange, text='Jaunais skaits:')
    jaunaisskaits_label.grid(column=0, row=1, sticky='W', **options)

    jaunaistips_label= ttk.Label(nameChange, text='Jaunais tips:')
    jaunaistips_label.grid(column=0, row=2, sticky='W', **options)

    jaunaiscena_label= ttk.Label(nameChange, text='Jaunā cena:')
    jaunaiscena_label.grid(column=0, row=4, sticky='W', **options)

    jaunaisrazotajs_label = ttk.Label(nameChange, text='Jaunais Ražotājs:')
    

    warning = ttk.Label(nameChange, text="!!!BLANK = OLD VALUE!!!")
    warning.grid(column=0, row=5, sticky='W', **options)
    warning1 = ttk.Label(nameChange, text="!!!BLANK = OLD VALUE!!!")
    warning1.grid(column=2, row=5, sticky='W', **options)

    #viens suds
    def refreshPopup():
        if selected_option.get() == "Dators/Detaļa":
            jaunaisrazotajs_label.grid(column=2, row=2, sticky='W', **options)
            jrazotajs_entry.grid(column=2, row=3, **options)
            print("world")

    def cancelRefresh():
        jrazotajs_entry.grid_forget()
        jaunaisrazotajs_label.grid_forget()
        print("pisprom")

    #buttons
    jvards = tk.StringVar()
    jvards_entry = ttk.Entry(nameChange, textvariable=jvards)
    jvards_entry.grid(column=1, row=0, **options)
    jvards_entry.focus()
    
    jrazotajs = tk.StringVar()
    jrazotajs_entry = ttk.Entry(nameChange, textvariable=jrazotajs)
    jrazotajs_entry.focus()

    jskaits = tk.StringVar()
    jskaits.set(0)
    jskaits_entry = ttk.Entry(nameChange, textvariable=jskaits)
    jskaits_entry.grid(column=1, row=1, **options)
    jvards_entry.focus()

    selected_option = tk.StringVar()
    radio1 = tk.Radiobutton(nameChange, text="Dators/Detaļa", variable=selected_option, value="Dators/Detaļa", command=refreshPopup)
    radio2 = tk.Radiobutton(nameChange, text="Programmatūra", variable=selected_option, value="Programmatūra", command=cancelRefresh)
    radio1.grid(column=1, row=2, **options)
    radio2.grid(column=1, row=3, **options)
    selected_option.set("1")

    jcena = tk.StringVar()
    jcena.set(0)
    jcena_entry = ttk.Entry(nameChange, textvariable=jcena)
    jcena_entry.grid(column=1, row=4, **options)
    jcena_entry.focus()

    jvards_poga = ttk.Button(nameChange, text='Mainīt datus', command=jaunaisvards)
    jvards_poga.grid(column=1, row=5, **options)

    nameChange.mainloop()


# listboxa atjaunināšana
def nomainit_sarakstu():
    listbox.delete(0, END)
    for Dators in visi_datori:
        if isinstance(Dators, Detala):
            listbox.insert(END, Dators.info1())
        else:
            listbox.insert(END, Dators.info())
#Buttons
vards_button = ttk.Button(frame, text='Pievienot sarakstam', command=pievienot_sarakstam)
vards_button.grid(column=2, row=0, sticky='W', **options)

vardamaina_poga = ttk.Button(frame, text='Nomainīt nosaukumu', command=vardamaina_clicked)
vardamaina_poga.grid(column=2, row=1, sticky='W', **options)

pirkt_poga = ttk.Button(frame, text="Nopirkts", command=nopirkts)
pirkt_poga.grid(column=2, row=2, sticky="W", **options)

frame.grid(padx=10, pady=10)

result_label = ttk.Label(frame)
result_label.grid(row=4, columnspan=3,column=2, **options)
# piešķilt grabažu
root.mainloop()