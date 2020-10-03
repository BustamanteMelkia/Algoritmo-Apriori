import copy

class Apriori():
    def __init__(self, transacciones, umbral):
        self.transacciones = transacciones
        self.umbral = umbral

    def iniciarAlgoritmo(self):
        candidatos = []
        candidatos.append(self.toLista(self.obtenerElementos()))
        frecuentes = []
        frecuentes.append(sorted(self.conjuntoFrecuente(candidatos[0])))
        combinaciones = []
        existenFrecuentes = True
        k=0
        while existenFrecuentes:
            combinaciones = self.combinarFrecuentes(frecuentes[k])
            candidatos.append(combinaciones)
            k+=1
            
    def soporte(self, subconjunto):
        frecuencia = 0
        for transaccion in self.transacciones:
            if all(list(map(lambda elemento:elemento in transaccion, subconjunto))):
                frecuencia += 1
        print(subconjunto, frecuencia)
        return frecuencia/len(self.transacciones)

    def obtenerCandidatos(self, transacciones):
        pass

    def obtenerElementos(self):
        elementos = []
        for transaccion in self.transacciones:
            for item in transaccion:
                if item not in elementos:
                    elementos.append(item)
        return elementos

    def conjuntoFrecuente(self, candidatos):
        return list(filter(lambda candidato:self.soporte(candidato)>=self.umbral, candidatos))

    def combinarFrecuentes(self, frecuentes):
        lista = []
        tamanio = len(frecuentes)
        for index in range(tamanio):
            a = [] 
            a = frecuentes[index] #1
            if (index+1) == tamanio:
                break
            for siguiente in range(index+1, tamanio):
                b = []
                b = frecuentes[siguiente] #2
                for elemento in b:
                    if elemento not in a:
                        temporalA = copy.deepcopy(a)
                        temporalA.append(elemento)
                        temporalA = sorted(temporalA)
                        if temporalA not in lista:
                            lista.append(temporalA)
        print(lista)

    def toLista(self, conjunto):
        lista = []
        for elemento in conjunto:
            temp = []
            temp.append(elemento)
            lista.append(temp)
        return lista
           


