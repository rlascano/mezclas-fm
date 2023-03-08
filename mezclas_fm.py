import tkinter as tk
from tkinter import *
from tkinter import ttk
from mezcla import Mezcla 
from tanque import Tanque

class App(tk.Tk):
   #I will refactor this later
   def __init__(self):
      super().__init__()

      self.mezcla = Mezcla(0, 0, 0, 0, 0, 0)      
      self.title('Mezclas RAC')
      self.mainframe = ttk.Frame(self, padding="24 24 24 24")
      self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
      self.columnconfigure(0, weight=1)
      self.rowconfigure(0, weight=1)
      ttk.Label(self.mainframe, text='Medida inicial').grid(column=2, row=1, sticky=W)
      self.medida_inicial = StringVar()
      self.medida_inicial_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.medida_inicial)
      self.medida_inicial_entry.grid(column=3, row=1, sticky=(W, E))
      ttk.Label(self.mainframe, text='Concentracion inicial').grid(column=2, row=2, sticky=W)
      self.conc_inicial = StringVar()
      self.conc_inicial_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.conc_inicial)
      self.conc_inicial_entry.grid(column=3, row=2, sticky=(W, E))
      self.mf_label = ttk.Label(self.mainframe, text='Medida final').grid(column=2, row=3, sticky=W)
      self.medida_final = StringVar()
      self.medida_final_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.medida_final)
      self.medida_final_entry.grid(column=3, row=3, sticky=(W, E))
      ttk.Label(self.mainframe, text='Cantidad de mezclas').grid(column=2, row=4, sticky=W)
      self.radio_frame = Frame(self.mainframe)
      self.radio_frame.grid(column=3, row=4)
      self.cantidad = IntVar()
      self.radio1 = ttk.Radiobutton(self.radio_frame, text='1 tk28', variable=self.cantidad, value=1, command=self.cantidad_mezclas)
      self.radio1.grid(column=3, row=0, sticky=W, padx=5)
      self.radio2 = ttk.Radiobutton(self.radio_frame, text='2 tk28', variable=self.cantidad, value=2, command=self.cantidad_mezclas)
      self.radio2.grid(column=4, row=0, sticky=W, padx=5)
      self.radio3 = ttk.Radiobutton(self.radio_frame, text='3 tk28', variable=self.cantidad, value=3, command=self.cantidad_mezclas)
      self.radio3.grid(column=5, row=0, sticky=W, padx=5)
      self.radio3 = ttk.Radiobutton(self.radio_frame, text='1 tk19', variable=self.cantidad, value=4, command=self.cantidad_mezclas)
      self.radio3.grid(column=6, row=0, sticky=W, padx=5)
      ttk.Label(self.mainframe, text='Concentracion deseada').grid(column=2, row=5, sticky=W)
      self.conc_deseada = StringVar()
      self.conc_deseada.set('65.5')
      self.conc_deseada_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.conc_deseada)
      self.conc_deseada_entry.grid(column=3, row=5, sticky=(W, E))

      ttk.Label(self.mainframe, text='Concentracion ácido concentrado').grid(column=2, row=6, sticky=W)

      self.conc_concentrado = StringVar()
      self.conc_concentrado_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.conc_concentrado)
      self.conc_concentrado_entry.grid(column=3, row=6, sticky=(W, E))

      ttk.Label(self.mainframe, text='Concentracion ácido diluido').grid(column=2, row=7, sticky=W)

      self.conc_diluido = StringVar()
      self.conc_diluido_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.conc_diluido)
      self.conc_diluido_entry.grid(column=3, row=7, sticky=(W, E))

      ttk.Button(self.mainframe, text='Calcular', command=self.calcular).grid(column=3, row=8, sticky=E)

      self.res = StringVar()
      ttk.Label(self.mainframe, textvariable=self.res).grid(column=2, row=9, columnspan = 2, sticky=(W, E))

      for child in self.mainframe.winfo_children():
           child.grid_configure(padx=3, pady=5)

      self.medida_inicial_entry.focus()
      self.bind("<Return>", self.calcular)

   def cantidad_mezclas(self):
    if self.cantidad.get() == 1:
       self.medida_final.set('150')
       self.mezcla.tanque = Tanque(28, 178.7)
    elif self.cantidad.get() == 2:
       self.medida_final.set('250')
       self.mezcla.tanque = Tanque(28, 178.7)
    elif self.cantidad.get() == 3:
       self.medida_final.set('365')  
       self.mezcla.tanque = Tanque(28, 178.7)
    else:
       self.medida_final.set('295')  
       self.mezcla.tanque = Tanque(19, 68)

   def calcular(self):
      self.mezcla.medida_inicial = float(self.medida_inicial.get())
      self.mezcla.concentracion_inicial = float(self.conc_inicial.get())
      self.mezcla.medida_final = float(self.medida_final.get())
      self.mezcla.concentracion_deseada = float(self.conc_deseada.get())
      self.mezcla.concentracion_concentrado = float(self.conc_concentrado.get())
      self.mezcla.concentracion_diluido = float(self.conc_diluido.get())

      cm_dil, cm_conc = self.mezcla.cm_final()

      self.res.set(f'Llevar a {cm_dil}cm con diluido y completar a {cm_conc}cm con concentrado')

if __name__ == "__main__":
    app = App()
    app.mainloop()
