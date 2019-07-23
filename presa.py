class Presa(Animal):
    """Clase presa
       1)Decidir - si - huye
                 - no - pasta  """
    def decidir(self,terreno):
        posicionP=terreno.posicion(self) # mis coordenadas en el terreno
        lista_vecinos=terreno.vecinos(self,rangoVision)
        if len(lista_vecino)!=0:
            distancias={} 
            for vecino in lista_vecinos
            posicionV=terreno.posicion(vecino)
            dis=(sqrt((posicionV[0]-posicionP[0])**2+(posicionV[1]-posicionP[1])**2)
            distancias[dis]=vecino
            mindis=min(distancias.keys())
            vecinomin=distancias[mindis]
            if(mindis>self.vmax):
                PosicionHuye=posicionP-self.vmax # como se define moverse en dirección opuesta al depredador sin sobrepasar la velocidad máxima
                posicionvmin=terreno.posicion(-vecinomin)
                terreno.mover(self,posicionvmin,vmax) 
            else:
            pastar(self)


 self.Observar(terreno)   

        if(posicionV>self.vmax)
#        elif


    def ejecutar(self,mover):
        """huye"""
        self.posicion=-self.posicion  
        self.velocidad=10   

    def pastar(self):
        """Se detiene y se alimenta"""
        if self.energia < self.energia_maxima
            modificar_energia+=1.1*self.energia
            print(energy)
        else:
            pass
    

