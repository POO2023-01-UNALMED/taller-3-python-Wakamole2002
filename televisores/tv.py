from televisores.control import Control
class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = Control()
        self._numTV += 1

    #Setters
    def setMarca(self, marca):
        self._marca = marca
    def setControl(self, control):
       self._control = control
    def setEstado(self, estado):
        self._estado = estado
    def setPrecio(self, precio):
        self._precio = precio
    def setCanal(self, canal):
        if (self._estado and (1<= self._canal <= 120)):
            self._canal = canal
    def setVolumen(self, volumen):
        if (self._estado and (0<= self._volumen<=7)):
            self._volumen = volumen
    @classmethod
    def setNumTV(cls, num):
        cls._numTV = num

    #Getters
    def getMarca(self):
        return self._marca
    def getControl(self):
       return self._control
    def getEstado(self):
        return self._estado    
    def getPrecio(self):
        return self._precio
    def getCanal(self):
        return self._canal
    def getVolumen(self):
        return self._volumen
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    #Encender y apagar
    def turnOn(self):
       self._estado = True
    def turnOff(self):
       self._estado = False
    
    #Subir y bajar canal
    def canalUp(self):
       if (self._estado) and (self._canal<120):
            self._canal += 1
    def canalDown(self):
       if (self._estado) and (self._canal>1):
          self._canal -= 1 
    
    #SUbir y bajar volumen
    def volumenUp(self):
       if (self._estado) and (self._volumen<7):
          self._volumen += 1
    def volumenDown(self):
       if (self._estado) and (self._volumen>0):
          self._volumen -= 1 
