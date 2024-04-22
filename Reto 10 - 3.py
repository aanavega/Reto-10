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