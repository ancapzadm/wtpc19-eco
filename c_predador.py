# Se importa la superclase de la cual hereda

from sc_animal import Animal

class Predador(Animal):
    """Subclase Predador que hereda de la superclase Animal."""
    
    def decidir(self,terreno):
        """Etapa de planificación. Observa el terreno y decide una acción pensando como predador. Si observa una presa y ésta se encuentra a una distancia inferior a su velocidad máxima, planea comerla; caso contrario, si se encuentra dentro de su rango de visión, planea perseguirla: se mueve para reducir su distancia con la presa más cercana; si tampoco cumple esta última condición, se planea moverse en alguna dirección aleatoria, una cantidad de pasos aleatorios inferior a su velocidad."""
        # Localiza a las presas visibles entre sus vecinos visibles
        vecinos_visibles = terreno.ubicar_vecinos(self)
        presas_visibles = [vecino for vecino in vecinos_visibles if vecino.get_clase() == "Presa"]
        # Si visualiza presas, calcula su distancia a ellas
        if len(presas_visibles) != 0:
            distancias_y_vecinos = {}
            for vecino in lista_vecinos:
                distancia = terreno.calcular_distancia(terreno.ubicar(self), terreno_ubicar(vecino))
                distancias_y_vecinos[distancia] = vecino
            # Determina el vecino más cercano
            distancia_menor = min(list(distancias_y_vecinos.keys()))
            vecino_mas_cercano = distancias_y_vecinos[distancia_menor]
            posicion_vecino_mas_cercano = terreno.ubicar(vecino_mas_cercano)
            # Si está más cerca que su velocidad máxima, planea comerlo (se ubica en la posición de la grilla de la presa y ésta desaparece) 
            if distancia_menor <= self.velocidad:
                plan=1 
                terreno.ejecutar(self,terreno)
                terreno.mover(self, posicion_vecino_mas_cercano)
                #self.modificar_energía(valor_porcentual)
            # Si no está lo suficientemente próxiomo, planea perseguirlo    
            else:
                plan=2
                terreno.ejecutar(self,terreno)
                posicion_cercana=terreno.generar_posicion_cercana_o_lejana(self,vecino_mas_cercano,0.5)#0.5 para cercana_1 para lejana    
                terreno.mover(self, posicion_cercana)
            
        # En caso de no observar presas cercanas, planea moverse en una dirección random
        else:
           plan=3
           terreno.ejecutar(self,terreno)
           posicion_random = terreno.generar_posicion_random()
           terreno.mover(self, posicion_random)
           

    def ejecutar(self,terreno):
        """Realiza la acción del plan."""
        if (plan==1 and self.energia<=self.energia_maxima):
           terreno.eliminar(vecino_mas_cercano)# aqui se debora al animal y ocupa su lugar
           self.energia+=5#se incrementa su energia 
        else:
           self.energia-=5#como de todos modods se movio para perseguir la presa pierde energia
            
       # pass
        # Debe modificarse el método decidir() para que guarde la orden de moverse en el atributo plan y luego aquí se intereprete y se ejecute.
