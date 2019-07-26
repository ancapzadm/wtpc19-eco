# Se importa la superclase de la cual hereda

from sc_animal import Animal

class Presa(Animal):
    """Subclase Presa que hereda de la superclase Animal."""

    def decidir(self,terreno):
        """Etapa de planificación. Observa el terreno y decide una acción pensando como presa. Si observa un predador, se escapa; caso contrario, se queda quieta y decide pastar."""
        # Localiza a los predadores visibles entre sus vecinos visibles
        vecinos_visibles = terreno.ubicar_vecinos(self)
        predadores_visibles = [vecino for vecino in vecinos_visibles if vecino.get_clase() == "Predador"]
        # Si visualiza predadores, calcula su distancia a ellas
        if len(predadores_visibles) != 0:
            distancias_y_predadores = {}
            for predador in predadores_visibles:
                posicion_A = terreno.ubicar(self)
                posicion_B = terreno.ubicar(predador)
                distancia = terreno.calcular_distancia(posicion_A, posicion_B)
                distancias_y_predadores[distancia] = predador
            # Determina el predador más cercano
            distancia_menor = min(list(distancias_y_predadores.keys()))
            predador_mas_cercano = distancias_y_predadores[distancia_menor]
            posicion_predador_mas_cercano = terreno.ubicar(predador_mas_cercano)
            # Se aleja del predador más próximo
            posicion_lejana = terreno.generar_posicion_lejana(self, posicion_predador_mas_cercano)
            self.plan = ("Huir", posicion_lejana)
       # Si no visualiza predadores, decide pastar (no se mueve y aumenta su energía)
        else: self.plan = ("Pastar",None)

    def ejecutar(self,terreno):
        """Realiza la acción del plan."""
        if self.plan[0] == "Huir":
            # Se aleja del depredador más próximo
            posicion_alejada = self.plan[1]
            terreno.mover(self, posicion_alejada)
            # Pierde energía por moverse
            self.modificar_energia(-self.coste_moverse)
        elif self.plan[0] == "Pastar":
            # No se mueve y gana energía por comer pasto
            self.modificar_energia(self.nutricion)
