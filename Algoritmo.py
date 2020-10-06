import copy

# Clase que implementa el algoritmo Apriori.

class Apriori():

    # umbral: soporte mínimo que debe cumplir un conjunto para considerarse un conjunto frecuente. 
    def __init__(self, transacciones, umbral):
        self.transacciones = transacciones
        self.umbral = umbral

    # Pasos para realizar el algoritmo Apri
    def iniciarAlgoritmo(self):
        candidatos = []
        frecuentes = []
        combinaciones = []
        # Conjunto de elementos posibles a combinar entre sí
        candidatos.append(self.toLista(self.obtenerElementos()))
        # Conjunto de candidatos que superar el umbral
        frecuentes.append(self.conjuntoFrecuente(candidatos[0])) # frecuentes tamanio 1
        existenFrecuentes = True
        k=0
        # Mientras existan conjuntos con elementos arriba del umbral
        while existenFrecuentes:
            combinaciones = self.combinarFrecuentes(frecuentes[k])
            candidatos.append(combinaciones) #candidatos de tamaño (k+1) [0],[1]
            k+=1
            frecuentes.append(self.conjuntoFrecuente(candidatos[-1])) # frecuentes tamaño (k+1)
            if len(frecuentes[-1]) == 0:    # Si no hay frecuentes
                existenFrecuentes = False
        return frecuentes

    # obtiene el cociente entre la frecuencia del subconjunto en las transacciones y el total de transacciones
    def soporte(self, subconjunto):
        frecuencia = 0
        for transaccion in self.transacciones:
            if all(list(map(lambda elemento:elemento in transaccion, subconjunto))):
                frecuencia += 1
        return frecuencia/len(self.transacciones)

    # Obtiene el conjunto de los elementos de la transacción.
    def obtenerElementos(self):
        elementos = []
        for transaccion in self.transacciones:
            for item in transaccion:
                if item not in elementos:
                    elementos.append(item)
        return elementos

    # Comprueba si el conjunto que tiene elementos con soporte mayor o igual al umbral y ordena el resultado
    def conjuntoFrecuente(self, candidatos):
        return sorted(list(filter(lambda candidato:self.soporte(candidato)>=self.umbral, candidatos)))
        
    # Obtiene las posibles combinaciones de un conjunto 
    def combinarFrecuentes(self, frecuentes):
        lista = []
        tamanio = len(frecuentes)
        for index in range(tamanio):
            a = [] 
            a = frecuentes[index]  # Primer elemento del conjunto
            if (index+1) == tamanio:
                break
            for siguiente in range(index+1, tamanio):
                b = []
                b = frecuentes[siguiente]  # Segundo elemento del conjunto
                for elemento in b:
                    if elemento not in a:
                        # Se hace una copia de la lista para evitar tener una referencia
                        temporalA = copy.deepcopy(a)
                        temporalA.append(elemento)
                        temporalA = sorted(temporalA)
                        if temporalA not in lista: # Si el elemento obtenido aún no existe en la lista
                            lista.append(temporalA)
        return lista

    # Convierte una lista simple en una lista de listas
    def toLista(self, conjunto):
        return list(map(lambda elemento: [elemento], conjunto))