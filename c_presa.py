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
            distancias_y_vecinos = {}
            for vecino in vecinos_visibles:
                posicion_A = terreno.ubicar(self)
                posicion_B = terreno.ubicar(vecino)
                distancia = terreno.calcular_distancia(posicion_A, posicion_B)
                distancias_y_vecinos[distancia] = vecino
            # Determina el vecino más cercano
            distancia_menor = min(list(distancias_y_vecinos.keys()))
            vecino_mas_cercano = distancias_y_vecinos[distancia_menor]
            posicion_vecino_mas_cercano = terreno.ubicar(vecino_mas_cercano)
            # Se aleja del predador más próximo
            posicion_lejana = terreno.generar_posicion_lejana(self, posicion_vecino_mas_cercano)
            self.plan = ("Huir", posicion_lejana)
       # Si no visualiza predadores, decide pastar (no se mueve y aumenta su energía)
        else:
            self.plan = ("Pastar")

    def ejecutar(self,terreno):
        """Realiza la acción del plan."""
        if self.plan[0] == "Huir":
            print("¡Animal huyó!")
            # Se aleja del depredador más próximo
            posicion_alejada = self.plan[1]
            terreno.mover(self, posicion_alejada)
            # Pierde energía por moverse
            self.modificar_energia(-self.coste_moverse)
        elif self.plan[0] == "Pastar":
            print("¡Animal pastó!")
            # No se mueve y gana energía por comer pasto
            self.modificar_energia(self.nutricion)
