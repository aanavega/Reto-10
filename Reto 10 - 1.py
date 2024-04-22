# Definir la funcion para calcular el promedio de un arreglo de numeros reales
def calcularpromedio(arreglo):

# Se suman los elementos del arreglo y se divide en la cantidad de estos
    return sum(arreglo)/len(arreglo)

# Se hace el calculo con un arreglo predeterminado
arreglo = [1, -3, 4.5, 10, 2.0]
promedio = calcularpromedio(arreglo)
print("El promedio del arreglo de numeros reales es: " + str(promedio))
