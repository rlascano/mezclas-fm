import tkinter as tk
from tkinter import *
from tkinter import ttk
from mezclas_cm import MezclaCm
from mezclas_kg import MezclaKg
from mezclas_corregir import MezclaCorregir

class App(tk.Tk):
   #I will refactor this later
   def __init__(self):
      super().__init__()
      
      self.title('Mezclas RAC')      
      self.columnconfigure(0, weight=1)
      self.rowconfigure(0, weight=1)

      self.notebook = ttk.Notebook(self)

      self.mezclas_cm = MezclaCm(self.notebook)
      self.notebook.add(self.mezclas_cm, text="Mezcla con cm", padding=10)

      self.mezclas_kg = MezclaKg(self.notebook)
      self.notebook.add(self.mezclas_kg, text="Mezcla con Kg", padding=10)

      self.mezclas_corregir = MezclaCorregir(self.notebook)
      self.notebook.add(self.mezclas_corregir, text="Corregir", padding=10)

      self.notebook.pack(padx=10, pady=10)
      #self.pack()
      
if __name__ == "__main__":
    app = App()
    app.mainloop()
