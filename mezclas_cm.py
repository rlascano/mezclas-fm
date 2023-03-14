import tkinter as tk
from tkinter import *
from tkinter import ttk
from mezcla import Mezcla 
from tanque import Tanque

class MezclaCm(ttk.Frame):
   #I will refactor this later
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.mezcla = Mezcla(0, 0, 0, 0, 0, 0)

      ttk.Label(self, text='Tanque').grid(column=2, row=1, sticky=W)
      self.tanque_combo = ttk.Combobox(self, width=40, state='readonly', values=['19', '28'], justify=tk.RIGHT)
      self.tanque_combo.grid(column=3, row=1, sticky=W)      
      ttk.Label(self, text='Medida inicial').grid(column=2, row=2, sticky=W)
      self.medida_inicial = StringVar()
      self.medida_inicial_entry = ttk.Entry(self, width=20, textvariable=self.medida_inicial, justify=tk.RIGHT)
      self.medida_inicial_entry.grid(column=3, row=2, sticky=(W, E))
      ttk.Label(self, text='Concentracion inicial').grid(column=2, row=3, sticky=W)
      self.conc_inicial = StringVar()
      self.conc_inicial_entry = ttk.Entry(self, width=20, textvariable=self.conc_inicial, justify=tk.RIGHT)
      self.conc_inicial_entry.grid(column=3, row=3, sticky=(W, E))
      self.mf_label = ttk.Label(self, text='Medida final').grid(column=2, row=4, sticky=W)
      self.medida_final = StringVar()
      self.medida_final_entry = ttk.Entry(self, width=20, textvariable=self.medida_final, justify=tk.RIGHT)
      self.medida_final_entry.grid(column=3, row=4, sticky=(W, E))
      ttk.Label(self, text='Cantidad de mezclas').grid(column=2, row=5, sticky=W)
      self.radio_frame = Frame(self)
      self.radio_frame.grid(column=3, row=5)
      self.cantidad = IntVar()
      self.radio1 = ttk.Radiobutton(self.radio_frame, text='1 tk28', variable=self.cantidad, value=1, command=self.cantidad_mezclas)
      self.radio1.grid(column=3, row=0, sticky=W, padx=5)
      self.radio2 = ttk.Radiobutton(self.radio_frame, text='2 tk28', variable=self.cantidad, value=2, command=self.cantidad_mezclas)
      self.radio2.grid(column=4, row=0, sticky=W, padx=5)
      self.radio3 = ttk.Radiobutton(self.radio_frame, text='3 tk28', variable=self.cantidad, value=3, command=self.cantidad_mezclas)
      self.radio3.grid(column=5, row=0, sticky=W, padx=5)
      self.radio3 = ttk.Radiobutton(self.radio_frame, text='1 tk19', variable=self.cantidad, value=4, command=self.cantidad_mezclas)
      self.radio3.grid(column=6, row=0, sticky=W, padx=5)
      ttk.Label(self, text='Concentracion deseada').grid(column=2, row=6, sticky=W)
      self.conc_deseada = StringVar()
      self.conc_deseada.set('65.5')
      self.conc_deseada_entry = ttk.Entry(self, width=20, textvariable=self.conc_deseada, justify=tk.RIGHT)
      self.conc_deseada_entry.grid(column=3, row=6, sticky=(W, E))

      ttk.Label(self, text='Concentracion ácido concentrado').grid(column=2, row=7, sticky=W)

      self.conc_concentrado = StringVar()
      self.conc_concentrado_entry = ttk.Entry(self, width=20, textvariable=self.conc_concentrado, justify=tk.RIGHT)
      self.conc_concentrado_entry.grid(column=3, row=7, sticky=(W, E))

      ttk.Label(self, text='Concentracion ácido diluido').grid(column=2, row=8, sticky=W)

      self.conc_diluido = StringVar()
      self.conc_diluido_entry = ttk.Entry(self, width=20, textvariable=self.conc_diluido, justify=tk.RIGHT)
      self.conc_diluido_entry.grid(column=3, row=8, sticky=(W, E))

      style = ttk.Style()
      style.configure('W.TButton', background='blue', foreground='#ddd', font=('calibri', 10, 'bold'))
      style.map('W.TButton', foreground = [('active', '!disabled', '#ddd')],
                     background = [('active', 'darkblue')])
      ttk.Button(self, text='Calcular', command=self.calcular, padding=(24, 12), style='W.TButton') \
         .grid(column=3, row=9, sticky=E)

      self.res = StringVar()
      ttk.Label(self, textvariable=self.res, foreground='blue', font=('calibri', 10, 'bold')).grid(column=2, row=10, columnspan = 2, sticky=(W, E))

      for child in self.winfo_children():
           child.grid_configure(padx=5, pady=8)           

      self.medida_inicial_entry.focus()
      self.bind("<Return>", self.calcular)

   def cantidad_mezclas(self):
    if self.cantidad.get() == 1:
       self.medida_final.set('150')
       self.tanque_combo.set('28')
    elif self.cantidad.get() == 2:
       self.medida_final.set('250')
       self.tanque_combo.set('28')
    elif self.cantidad.get() == 3:
       self.medida_final.set('365')  
       self.tanque_combo.set('28')
    else:
       self.medida_final.set('295')  
       self.tanque_combo.set('19')

   def calcular(self):
      tanque = self.tanque_combo.get()
      if tanque == '19':
         self.mezcla.tanque = Tanque(19, 68.0)
      else: 
         self.mezcla.tanque = Tanque(28, 178.7)
      
      self.__format()
      self.mezcla.medida_inicial = float(self.medida_inicial.get())
      self.mezcla.concentracion_inicial = float(self.conc_inicial.get())
      self.mezcla.medida_final = float(self.medida_final.get())
      self.mezcla.concentracion_deseada = float(self.conc_deseada.get())
      self.mezcla.concentracion_concentrado = float(self.conc_concentrado.get())
      self.mezcla.concentracion_diluido = float(self.conc_diluido.get())

      cm_dil, cm_conc = self.mezcla.cm_final('cm')

      self.res.set(f'Llevar a {cm_dil}cm con diluido y completar a {cm_conc}cm con concentrado')

   def __format(self):
      self.medida_inicial.set(self.__cambiar_coma(self.medida_inicial.get()))
      self.conc_inicial.set(self.__cambiar_coma(self.conc_inicial.get()))
      self.medida_final.set(self.__cambiar_coma(self.medida_final.get()))
      self.conc_deseada.set(self.__cambiar_coma(self.conc_deseada.get()))
      self.conc_concentrado.set(self.__cambiar_coma(self.conc_concentrado.get()))
      self.conc_diluido.set(self.__cambiar_coma(self.conc_diluido.get()))

   def __cambiar_coma(self, value):
      return value.replace(',', '.')   
