import tkinter as tk
from tkinter import *
from tkinter import ttk
from mezcla import Mezcla 
from tanque import Tanque

class MezclaCorregir(ttk.Frame):
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

      ttk.Label(self, text='Concentracion deseada').grid(column=2, row=4, sticky=W)
      self.conc_deseada = StringVar()
      self.conc_deseada.set('65.5')
      self.conc_deseada_entry = ttk.Entry(self, width=20, textvariable=self.conc_deseada, justify=tk.RIGHT)
      self.conc_deseada_entry.grid(column=3, row=4, sticky=(W, E))

      ttk.Label(self, text='Concentracion ácido conc / dil').grid(column=2, row=5, sticky=W)
      self.conc_concentrado = StringVar()
      self.conc_concentrado_entry = ttk.Entry(self, width=20, textvariable=self.conc_concentrado, justify=tk.RIGHT)
      self.conc_concentrado_entry.grid(column=3, row=5, sticky=(W, E))        

      style = ttk.Style()
      style.configure('W.TButton', background='blue', foreground='#ddd', font=('calibri', 10, 'bold'))
      style.map('W.TButton', foreground = [('active', '!disabled', '#ddd')],
                     background = [('active', 'darkblue')])
      ttk.Button(self, text='Calcular', command=self.calcular, padding=(24, 12), style='W.TButton').grid(column=3, row=6, sticky=E)

      self.res = StringVar()
      ttk.Label(self, textvariable=self.res, foreground='blue', font=('calibri', 10, 'bold')).grid(column=2, row=10, columnspan = 2, sticky=(W, E))

      for child in self.winfo_children():
           child.grid_configure(padx=5, pady=8)

      self.medida_inicial_entry.focus()
      self.bind("<Return>", self.calcular)   

   def calcular(self):
      tanque = self.tanque_combo.get()
      if tanque == '19':
         self.mezcla.tanque = Tanque(19, 68.0)
      else: 
         self.mezcla.tanque = Tanque(28, 178.7)

      self.__format()   
         
      self.mezcla.medida_inicial = float(self.medida_inicial.get())
      self.mezcla.concentracion_inicial = float(self.conc_inicial.get())
      self.mezcla.concentracion_deseada = float(self.conc_deseada.get())
      self.mezcla.concentracion_concentrado = float(self.conc_concentrado.get())
      
      cm_corr = self.mezcla.corregir()

      producto = ''

      if self.conc_concentrado.get() == '0':
         producto = 'agua'
      else: 
         producto = 'ácido nítrico ' + self.conc_concentrado.get()   

      self.res.set(f'Corregir con {round(cm_corr, 2)}cm de {producto}')

   def __format(self):
      self.medida_inicial.set(self.__cambiar_coma(self.medida_inicial.get()))
      self.conc_inicial.set(self.__cambiar_coma(self.conc_inicial.get()))      
      self.conc_deseada.set(self.__cambiar_coma(self.conc_deseada.get()))
      self.conc_concentrado.set(self.__cambiar_coma(self.conc_concentrado.get()))    

   def __cambiar_coma(self, value):
      return value.replace(',', '.')
