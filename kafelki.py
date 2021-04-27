import tkinter as tk

def ile_kafelek(dim1,dim2,field): #oblicz ile kafelek o danych wymiarach potrzeba dla danej powierzchni
    return round((field*10000)/(dim1*dim2),2) #wymiary kafelki w cm kw a powierzchnia w metrac kw

window = tk.Tk()
window.title("Kafelki")
window.columnconfigure([0,1], weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)

# Data taking left frame
frm_dim_taker = tk.Frame(relief= tk.RAISED, borderwidth=5)
lbl_kafelka1 = tk.Label(master = frm_dim_taker, text="1 wymiar kafelki (w cm kw):")
lbl_kafelka1.grid(row=0,column=0)
entry_kafelka1 = tk.Entry(master = frm_dim_taker)
entry_kafelka1.grid(row=0, column=1)
lbl_kafelka2 = tk.Label(master = frm_dim_taker, text="2 wymiar kafelki (w cm kw):")
lbl_kafelka2.grid(row=1, column=0)
entry_kafelka2 = tk.Entry(master = frm_dim_taker)
entry_kafelka2.grid(row=1, column=1)
lbl_pow = tk.Label(master = frm_dim_taker, text="powierzchnia (w metrach kw):")
lbl_pow.grid(row=2, column=0)
entry_pow = tk.Entry(master = frm_dim_taker)
entry_pow.grid(row=2, column=1)

frm_dim_taker.grid(row=0, column = 0)

#buttons and their functions
def btn_go_cmd():
    try:
        wynik = ile_kafelek(float(entry_kafelka1.get().replace(",",".")), #"replace" na wypadek gdyby ktoś wpisał liczbę z przecinkiem
                            float(entry_kafelka2.get().replace(",",".")),
                            float(entry_pow.get().replace(",","."))
                            )
    except:
        lbl_result_giver['text'] = 'wystąpił błąd - podaj poprawne wartości'
    else:
        lbl_result_giver['text'] = "wymiary kafelki: {}/{} cm kw \n powierzchnia: {} metrów kw \n Potrzebna ilość kafelek wynosi {}".format(
            entry_kafelka1.get().replace(",","."),
            entry_kafelka2.get().replace(",","."),
            entry_pow.get(),
            wynik)
        entry_kafelka1.delete(0, tk.END)
        entry_kafelka2.delete(0, tk.END)
        entry_pow.delete(0, tk.END)
btn_go = tk.Button(text="Oblicz ilość kafelek", command = btn_go_cmd)
btn_go.grid(row=3, column=0, sticky="NEWS")

def btn_clear_cmd():
    lbl_result_giver['text'] = ''
btn_clear = tk.Button(text="wyczyść wynik", command = btn_clear_cmd)
btn_clear.grid(row=3, column=1, sticky="NEWS")

#results displaying right frame
lbl_result_giver = tk.Label(text = '', relief= tk.SUNKEN, borderwidth=5, width=50, height=5)
lbl_result_giver.grid(row=0, column=1, sticky ='news')


window.mainloop()