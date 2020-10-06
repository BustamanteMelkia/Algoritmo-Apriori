def miUmbral():
    with open('archivo.txt') as f:
        for linea in f:
            f.close()
            return float(linea)


def misTransacciones():
    
    umbralItem = True

    transacciones = []
    
    with open('archivo.txt') as f:
        for linea in f:
            if(umbralItem == True):
                umbralItem=False
            else:
                transaccion = [int(n) for n in linea.split(",")]
                transacciones.append(transaccion)


    f.close()

    return transacciones
