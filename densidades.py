import json


class Densidad:
  def __init__(self):
    #Obtener densidades desde archivo
    f = open('densidades.txt')
    self.values = json.load(f)
    f.close()

  #Obtener densidad segun concentracion
  def obtener_densidad(self, concentracion):  
    try:
        return float(self.values[str(round(concentracion, 1))])
    except:
        print('Debe ingresar la concentración con 1 decimal')