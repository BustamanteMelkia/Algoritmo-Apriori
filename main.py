from Algoritmo import Apriori

#Tansacciones desde archivo
transacciones = [[1,2], [2,4], [2,3], [1,2,4], [1,3], [2,3], [1,3], [1,2,3,5], [1,2,3]]
apriori = Apriori(transacciones, 2/9)
apriori.iniciarAlgoritmo()
