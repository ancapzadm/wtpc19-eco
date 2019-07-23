import random
class Cazador(Animal):
    """Clase del cazador"""        

    def decidir(self,terreno):
        """Etapa de planificación. Observa el terreno (método de la clase animal, que hereda) y decide una acción. Si observa una presa y ésta se encuentra a una distancia inferior a su velocidad máxima (atributo de la superclase animal), planea comerla; caso contrario, si se encuentra dentro de su rango de visión (atributo de la superclase animal), planea perseguirla: se mueve* para reducir su distancia con la presa más cercana; si tampoco cumple esta última condición, se planea moverse* en alguna dirección aleatoria, una cantidad de pasos aleatorios inferior a su velocidad."""
       posicionC=terreno.poscicion(self)#mis coordenadas, posion del cazador
       lista_vecinos=terreno.vecinos(self, rangoVision)
       if len(lista_vecino)!=0:
           distancias={}
           for vecino in lista_vecinos 
              posicionV=terreno.posicion(vecino)
              dis=(sqrt((posicioV[0]-posicionC[0])**2+(posicioV[1]-posicionC[1])**2)
              distancias[dis]=vecino
           mindis=min(distancias.keys())
           vecinomin=distancias[minsdis]
           if (mindis< self.vmax):
              self.comer(self,vecinomin)
            #recordar poner mover dentro del metodo comer
            else: 
                posicionvmin=terreno.posicion(vecinomin)
                terreno.mover(self,posicionvmin,vmax) 
       else:
            pos_aleat=random.random()#pensar ento en un par x,y dentro de la grilla del terreno
            terreno.mover(self,pos_aleat,vmax)
               

    def ejecutar(self,terreno):
        """realiza una accion se desplaza"""
        self.velocidad=velmax
        self.posicion= self.posicion + velmax#¿como se mueven los animales? en que direcciones ,lineal en x , lineal en y o en escalera?
     

    def comer(self,vecinomin):
        """atrapa a la presa y se alimenta"""
        self.tereno.grilla.pop(0)#elimina un animal del terreno
        if self.energia < self.energia_maxima
            modificar_energia+=1.1*self.energia
#            print(energy)
#        else:
#            pass






 
    
