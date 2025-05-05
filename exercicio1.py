import numpy as np

# a) Array de inteiros de 1 a 100
array_inteiros = np.arange(1, 101)

# pares
array_pares = array_inteiros[array_inteiros % 2 == 0]

# ímpares
array_impares = array_inteiros[array_inteiros % 2 != 0]

print("Inteiros:",  array_inteiros)
print("Pares:   ",  array_pares)
print("Ímpares: ",  array_impares)