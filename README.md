# Reto-10

### Punto numero 1

- Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```Python
# Definir la funcion para calcular el promedio de un arreglo de numeros reales
def calcularpromedio(arreglo):

# Se suman los elementos del arreglo y se divide en la cantidad de estos
    return sum(arreglo)/len(arreglo)

# Se hace el calculo con un arreglo predeterminado
arreglo = [1, -3, 4.5, 10, 2.0]
promedio = calcularpromedio(arreglo)
print("El promedio del arreglo de numeros reales es: " + str(promedio))
```

### Punto numero 2

- Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

```Python
# Definir ambos arreglos de igual tamaño con numeros reales
lista1 = [-2, 3, 6.5]
lista2 = [1, 2.8, -20]

# Realizar las operaciones para hallar el producto punto entre ambos arreglos
print((lista1[0]*lista2[0])+(lista1[1]*lista2[1])+(lista1[2]*lista2[2]))
```

### Punto numero 3

- Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

```Python
# Definir el arreglo para añadirle los ceros al final
arreglo = [1, 2, 0, 3, 0, 7, 4, 0, 65, 0, 32, 15, 99, 0]

# Remover los ceros que aparecen de izquierda a derecha
arreglo.remove(0)
arreglo.remove(0)
arreglo.remove(0)
arreglo.remove(0)
arreglo.remove(0)

# Insertar al final del arreglo los cinco ceros eliminados
arreglo.insert(9, "0")
arreglo.insert(10, "0")
arreglo.insert(11, "0")
arreglo.insert(12, "0")
arreglo.insert(13, "0")

# Mostrar el arreglo resultante con los ceros al final del mismo
print(arreglo)
```
