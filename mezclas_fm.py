from tkinter import *
from tkinter import ttk
import json

#Obtener densidades desde archivo
f = open('densidades.txt')
values = json.load(f)
f.close()

#Obtener densidad segun concentracion
def obtener_densidad(concentracion):
  try:
    return float(values[str(round(concentracion, 1))])
  except:
    print('Debe ingresar la concentración con 1 decimal')


#Tanques
tanques = [{'id':19, 'litros_por_cm': 68}, {'id': 28, 'litros_por_cm': 178.7}]

tanque = tanques[1]

def calcular(*args):
    medida_ini = float(medida_inicial.get())
    medida_fin = float(medida_final_entry.get())
    conc_ini = float(conc_inicial.get())
    conc_des = float(conc_deseada.get())
    conc_c = float(conc_concentrado.get())
    conc_d = float(conc_diluido.get())

    kg_inicial = medida_ini * obtener_densidad(conc_ini) * tanque['litros_por_cm']
    kg_final = medida_fin * obtener_densidad(conc_des) * tanque['litros_por_cm']

    kg_concentrado = (kg_final * conc_des - kg_inicial * conc_ini - \
    conc_d * kg_final + conc_d * kg_inicial) / (conc_c - conc_d)

    kg_diluido = (conc_c * kg_final - conc_c * kg_inicial - \
    kg_final * conc_des + kg_inicial * conc_ini) / (conc_c - conc_d)

    cm_concentrado = kg_concentrado / obtener_densidad(conc_c) / tanque['litros_por_cm']
    cm_diluido = kg_diluido / obtener_densidad(conc_d) / tanque['litros_por_cm']

    
    cm_totales = cm_concentrado + cm_diluido + medida_ini
    prop_c = 1 / ((cm_diluido / cm_concentrado) + 1)    
    corr_dil = (cm_totales - medida_fin) * (1 - prop_c)    
    corr_conc = (cm_totales - medida_fin) * prop_c

    cm_diluido_final = round(cm_diluido - corr_dil + medida_ini, 2)
    cm_completar = round(cm_diluido_final + cm_concentrado - corr_conc, 2)

    res.set(f'Debe agregar {cm_diluido_final}cm de diluido y completar a {cm_completar}cm con concentrado')


def cantidad_mezclas():
   if cantidad.get() == 1:
      medida_final.set('150')
      tanque = tanques[1]
   elif cantidad.get() == 2:
      medida_final.set('250')
      tanque = tanques[1]
   elif cantidad.get() == 3:
      medida_final.set('365')  
      tanque = tanques[1] 
   else:
      medida_final.set('295')  
      tanque = tanques[0]    

root = Tk()
root.title('Mezclas FM')

mainframe = ttk.Frame(root, padding="24 24 24 24")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Medida inicial').grid(column=2, row=1, sticky=W)

medida_inicial = StringVar()
medida_inicial_entry = ttk.Entry(mainframe, width=20, textvariable=medida_inicial)
medida_inicial_entry.grid(column=3, row=1, sticky=(W, E))

ttk.Label(mainframe, text='Concentracion inicial').grid(column=2, row=2, sticky=W)

conc_inicial = StringVar()
conc_inicial_entry = ttk.Entry(mainframe, width=20, textvariable=conc_inicial)
conc_inicial_entry.grid(column=3, row=2, sticky=(W, E))

ttk.Label(mainframe, text='Medida final').grid(column=2, row=3, sticky=W)

medida_final = StringVar()
medida_final_entry = ttk.Entry(mainframe, width=20, textvariable=medida_final)
medida_final_entry.grid(column=3, row=3, sticky=(W, E))

ttk.Label(mainframe, text='Cantidad de mezclas').grid(column=2, row=4, sticky=W)
#Todo poner radio buttons
radio_frame = Frame(mainframe)
radio_frame.grid(column=3, row=4)
cantidad = IntVar()
radio1 = ttk.Radiobutton(radio_frame, text='1 tk28', variable=cantidad, value=1, command=cantidad_mezclas)
radio1.grid(column=3, row=0, sticky=W, padx=5)

radio2 = ttk.Radiobutton(radio_frame, text='2 tk28', variable=cantidad, value=2, command=cantidad_mezclas)
radio2.grid(column=4, row=0, sticky=W, padx=5)

radio3 = ttk.Radiobutton(radio_frame, text='3 tk28', variable=cantidad, value=3, command=cantidad_mezclas)
radio3.grid(column=5, row=0, sticky=W, padx=5)

radio3 = ttk.Radiobutton(radio_frame, text='1 tk19', variable=cantidad, value=4, command=cantidad_mezclas)
radio3.grid(column=6, row=0, sticky=W, padx=5)

ttk.Label(mainframe, text='Concentracion deseada').grid(column=2, row=5, sticky=W)

conc_deseada = StringVar()
conc_deseada.set('65.5')
conc_deseada_entry = ttk.Entry(mainframe, width=20, textvariable=conc_deseada)
conc_deseada_entry.grid(column=3, row=5, sticky=(W, E))

ttk.Label(mainframe, text='Concentracion ácido concentrado').grid(column=2, row=6, sticky=W)

conc_concentrado = StringVar()
conc_concentrado_entry = ttk.Entry(mainframe, width=20, textvariable=conc_concentrado)
conc_concentrado_entry.grid(column=3, row=6, sticky=(W, E))

ttk.Label(mainframe, text='Concentracion ácido diluido').grid(column=2, row=7, sticky=W)

conc_diluido = StringVar()
conc_diluido_entry = ttk.Entry(mainframe, width=20, textvariable=conc_diluido)
conc_diluido_entry.grid(column=3, row=7, sticky=(W, E))

ttk.Button(mainframe, text='Calcular', command=calcular).grid(column=3, row=8, sticky=E)

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=9, columnspan = 2, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=3, pady=5)

medida_inicial_entry.focus()
root.bind("<Return>", calcular)

root.mainloop()

