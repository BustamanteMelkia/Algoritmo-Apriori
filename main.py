from Algoritmo import Apriori

#Tansacciones desde archivo
# transacciones = [[1,2,5], [2,4], [2,3], [1,2,4], [1,3], [2,3], [1,3], [1,2,3,5], [1,2,3]]  #2/9
#transacciones = [[1,2,3,4],[1,2,4],[1,2],[2,3,4],[2,3],[3,4],[2,4]]  #3/7
transacciones = [[1,2,4],[2,4,5],[1,3],[1,2,4],[1,2,3],[2,4],[1,3],[1,2,4,5],[1,2,3]]  #2/9
#Creación de un objeto Apriori que recibe la transacción cargada y el umbral
apriori = Apriori(transacciones, 2/9)
frecuentes = []
frecuentes = apriori.iniciarAlgoritmo()

# Output
for index in range(0, len(frecuentes)-1):
    print(f'Conjunto(s) frecuente(s) de {index+1} elemento(s):\t',frecuentes[index])
