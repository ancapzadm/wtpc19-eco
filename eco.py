# Grupo ECO - WTPC 2019
# Este es el script que simula un ecosistema con cazador(depredador) y presa

class Animal(object):
    def __init__(self, velocidad, vision, energia, energia_maxima, plan):
        self.velocidad = velocidad
		self.vision = vision
		self.energia = energia
		self.energia_maxima = energia_maxima
		self.plan = plan
   
    def observar(self,terreno,vision):
        vecinos = terreno.informar_vecinos(vision)
		

    def modificar_energia(self,obj,nombre):
        
		pass
		
class Cazador(Animal)
    def decidir(self, )
        
        pass

    def ejecutar(self, )
	    
	    pass

    def comer(self,)
        
        pass
		
class Presa(Animal)
    def decidir(self)
	    
		pass
		
	def ejecutar(self)
	    
		pass
		
	def pastar(self)
	    
		pass