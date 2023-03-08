class Tanque:
    def __init__(self, id, litros_por_cm):
        self.id = id
        self.litros_por_cm = litros_por_cm

    @property
    def id(self):
        return self._id
    
    @property
    def litros_por_cm(self):
        return self._litros_por_cm

    @id.setter
    def id(self, id):
        self._id = id

    @litros_por_cm.setter
    def litros_por_cm(self, litros_por_cm):
        self._litros_por_cm = litros_por_cm