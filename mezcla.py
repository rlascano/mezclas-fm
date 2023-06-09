from tanque import Tanque
from densidades import Densidad

class Mezcla:
    def __init__(self, medida_inicial, concentracion_inicial, medida_final, 
                 concentracion_deseada, concentracion_concentrado, concentracion_diluido):
        #por defecto se usa el tk 28
        self.tanque = Tanque(28, 178.7)
        self.medida_inicial = medida_inicial
        self.concentracion_inicial = concentracion_inicial
        self.medida_final = medida_final
        self.concentracion_deseada = concentracion_deseada
        self.concentracion_concentrado = concentracion_concentrado
        self.concentracion_diluido = concentracion_diluido
        self.densidades = Densidad()
    
    @property
    def tanque(self):
        return self._tanque
    
    @tanque.setter
    def tanque(self, tanque):
        self._tanque = tanque  

    @property
    def medida_inicial(self):
        return self._medida_inicial     

    @medida_inicial.setter
    def medida_inicial(self, medida_inicial):
        self._medida_inicial = medida_inicial  

    @property
    def concentracion_inicial(self):
        return self._concentracion_inicial      
    
    @concentracion_inicial.setter
    def concentracion_inicial(self, concentracion_inicial):
        self._concentracion_inicial = concentracion_inicial  
    
    
    @property
    def medida_final(self):
        return self._medida_final
    
    @medida_final.setter
    def medida_final(self, medida_final):
        self._medida_final = medida_final  

    @property
    def concentracion_deseada(self):
        return self._concentracion_deseada      
    
    @concentracion_deseada.setter
    def concentracion_deseada(self, concentracion_deseada):
        self._concentracion_deseada = concentracion_deseada   

    @property
    def concentracion_concentrado(self):
        return self._concentracion_concentrado     

    @concentracion_concentrado.setter
    def concentracion_concentrado(self, concentracion_concentrado):
        self._concentracion_concentrado = concentracion_concentrado  

    @property
    def concentracion_diluido(self):
        return self._concentracion_diluido      

    @concentracion_diluido.setter
    def concentracion_diluido(self, concentracion_diluido):
        self._concentracion_diluido = concentracion_diluido   

    def cm_a_kg(self, medida, concentracion):   
        return medida * \
                self.densidades.obtener_densidad(concentracion) * \
                self.tanque.litros_por_cm    
    
    #I will refactor this later ♪♪♪
    def kilos_concentrado(self, unidad):
        kg_inicial = self.cm_a_kg(self.medida_inicial, float(self.concentracion_inicial))
        if unidad == 'cm':
            kg_final = self.cm_a_kg(self.medida_final, float(self.concentracion_deseada))  
        else:
            kg_final = float(self.medida_final)             

        num = (kg_final * self.concentracion_deseada - kg_inicial * self.concentracion_inicial -
               self.concentracion_diluido * kg_final + self.concentracion_diluido * kg_inicial)
        den = self.concentracion_concentrado - self.concentracion_diluido 
        return num/den
    
    #I will refactor this later ♪♪♪
    def kilos_diluido(self, unidad):
        kg_inicial = self.cm_a_kg(self.medida_inicial, float(self.concentracion_inicial))
        if unidad == 'cm':
            kg_final = self.cm_a_kg(self.medida_final, float(self.concentracion_deseada)) 
        else: 
            kg_final = float(self.medida_final)

        num = (self.concentracion_concentrado * kg_final - self.concentracion_concentrado * kg_inicial -
               kg_final * self.concentracion_deseada + kg_inicial * self.concentracion_inicial)
        den = self.concentracion_concentrado - self.concentracion_diluido 
        return num/den

    def cm_concentrado(self, unidad):
        return self.kilos_concentrado(unidad) / self.densidades.obtener_densidad(self.concentracion_concentrado) / self.tanque.litros_por_cm

    def cm_diluido(self, unidad):        
        return self.kilos_diluido(unidad) / self.densidades.obtener_densidad(self.concentracion_diluido) / self.tanque.litros_por_cm

    def cm_final(self, unidad):
        if unidad == 'cm':
            medida_final = self.medida_final
        else:
            medida_final = self.medida_final / self.densidades.obtener_densidad(self.concentracion_deseada) / self.tanque.litros_por_cm    
        
        cm_diluido = self.cm_diluido(unidad)
        cm_concentrado = self.cm_concentrado(unidad)
        cm_totales = self.medida_inicial + cm_diluido + cm_concentrado
        prop = 1 / ((cm_diluido / cm_concentrado) + 1) 
        dil_corr = (cm_totales - medida_final) * (1 - prop)    
        conc_corr = (cm_totales - medida_final) * prop

        cm_diluido_final = round(cm_diluido - dil_corr + self.medida_inicial, 2)
        cm_completar = round(cm_diluido_final + cm_concentrado - conc_corr, 2)

        return cm_diluido_final, cm_completar

    def corregir(self):
        kg_inicial = self.cm_a_kg(self.medida_inicial, float(self.concentracion_inicial))
        aux = kg_inicial * (self.concentracion_concentrado - self.concentracion_inicial) / (self.concentracion_concentrado - self.concentracion_deseada)
        aux_1 = aux * (self.concentracion_inicial - self.concentracion_deseada) / (self.concentracion_inicial - self.concentracion_concentrado)
        cm = aux_1 / self.densidades.obtener_densidad(self.concentracion_concentrado) / self.tanque.litros_por_cm
        return cm
        