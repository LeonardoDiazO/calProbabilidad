from collections import Counter

def calcular_probabilidades(lista_numeros):
    # Contar la frecuencia de cada número
    frecuencia = Counter(lista_numeros)
    
    # Calcular el total de elementos en la lista
    total_numeros = len(lista_numeros)
    
    # Calcular la probabilidad de cada número
    probabilidades = {num: freq / total_numeros for num, freq in frecuencia.items()}
    
    return probabilidades

# Lista de números (sin ceros a la izquierda)
lista_numeros = [
    10, 11, 18, 32, 38, 10, 11, 16, 26, 28, 5, 9, 19, 28, 34, 4, 9, 21, 30, 35,
    7, 12, 21, 30, 32, 1, 3, 8, 11, 26, 1, 11, 12, 19, 30, 1, 4, 15, 22, 30, 
    8, 22, 25, 35, 36, 7, 12, 21, 28, 37, 13, 16, 21, 25, 34, 11, 20, 27, 33, 
    37, 3, 6, 14, 19, 38, 9, 11, 12, 32, 38, 1, 3, 17, 20, 38, 6, 7, 11, 23, 
    36, 8, 18, 31, 33, 34, 1, 4, 6, 7, 37, 5, 19, 23, 31, 38, 13, 23, 27, 33, 
    37, 8, 10, 18, 38, 39, 8, 23, 27, 29, 35, 3, 14, 23, 28, 29, 6, 12, 15, 27, 
    39, 2, 3, 10, 16, 28, 9, 11, 25, 31, 36, 3, 6, 14, 17, 20, 7, 17, 19, 33, 
    34, 21, 23, 29, 31, 34, 7, 8, 21, 22, 34, 7, 9, 13, 24, 30, 4, 10, 17, 29, 
    38, 9, 13, 18, 23, 25, 2, 6, 19, 26, 34, 7, 14, 20, 21, 37, 9, 10, 13, 15, 
    34, 8, 17, 25, 29, 30, 3, 7, 8, 24, 28, 3, 5, 17, 25, 29, 1, 2, 3, 6, 26, 
    19, 24, 25, 27, 31, 15, 17, 21, 26, 34, 2, 6, 13, 17, 37, 8, 14, 15, 21, 33, 
    5, 9, 22, 24, 31, 3, 8, 13, 28, 30, 3, 15, 17, 20, 23, 3, 8, 23, 26, 35, 
    4, 18, 21, 25, 32, 18, 19, 24, 33, 37, 5, 11, 12, 15, 32, 2, 3, 5, 12, 36, 
    4, 9, 13, 14, 27, 2, 19, 24, 29, 35, 16, 17, 35, 38, 39, 7, 15, 21, 23, 24, 
    2, 14, 21, 34, 38, 10, 17, 26, 32, 34, 28, 32, 35, 36, 38, 7, 9, 15, 25, 
    39, 4, 27, 37, 38, 39, 4, 18, 26, 31, 39, 1, 2, 12, 19, 38, 5, 9, 20, 22, 
    32, 5, 23, 33, 36, 37, 5, 10, 13, 25, 30, 3, 5, 7, 15, 37, 6, 8, 14, 26, 35, 
    12, 15, 28, 33, 34, 8, 16, 28, 29, 38, 2, 17, 25, 32, 33, 14, 17, 18, 36, 37, 
    1, 16, 18, 21, 26, 5, 7, 21, 26, 39, 5, 11, 27, 34, 38, 3, 9, 17, 27, 30, 3, 
    10, 12, 17, 24, 3, 15, 35, 36, 37, 1, 4, 9, 29, 35, 3, 8, 23, 26, 29, 5, 7, 
    21, 29, 38, 1, 7, 12, 20, 34, 15, 18, 25, 30, 33, 3, 5, 19, 21, 27, 2, 11, 
    24, 25, 30, 21, 25, 26, 31, 33, 3, 26, 30, 33, 39, 4, 6, 8, 12, 26, 6, 10, 
    29, 32, 36, 6, 7, 10, 32, 39, 3, 13, 30, 35, 38, 1, 14, 31, 37, 38, 7, 12, 
    17, 18, 34, 2, 9, 14, 15, 26, 2, 8, 10, 14, 17, 4, 7, 14, 21, 36, 15, 16, 
    19, 22, 37, 2, 11, 15, 17, 31, 9, 10, 12, 24, 34, 20, 25, 28, 29, 34, 13, 
    31, 33, 34, 35, 6, 10, 11, 31, 39, 6, 18, 21, 27, 37, 4, 6, 8, 17, 30, 3, 
    20, 21, 26, 30, 5, 9, 23, 31, 37, 3, 13, 18, 34, 35, 2, 20, 21, 25, 26, 7, 
    21, 23, 24, 27, 14, 18, 25, 30, 38, 1, 15, 22, 27, 38, 5, 13, 21, 22, 39, 
    9, 13, 14, 18, 21, 1, 2, 8, 32, 36, 2, 15, 16, 24, 30, 3, 18, 21, 24, 27, 4, 
    24, 33, 37, 39, 2, 20, 28, 32, 37, 1, 17, 19, 25, 38, 23, 32, 33, 35, 36, 28, 
    29, 32, 34, 35, 3, 9, 19, 28, 31, 9, 13, 19, 22, 23, 11, 22, 27, 33, 35, 7, 
    11, 14, 26, 36, 13, 23, 24, 34, 35, 1, 3, 6, 7, 23, 4, 9, 17, 22, 32, 5, 9, 
    13, 15, 32, 8, 12, 22, 25, 28, 8, 10, 14, 27, 31, 7, 8, 23, 24, 36, 2, 8, 13, 
    20, 29, 3, 17, 23, 32, 34, 5, 6, 8, 17, 36, 9, 21, 29, 34, 39, 5, 7, 19, 21, 
    36, 5, 13, 15, 22, 39, 6, 8, 11, 12, 19, 2, 9, 16, 30, 34, 1, 10, 18, 28, 35
]

# Calcular las probabilidades
probabilidades = calcular_probabilidades(lista_numeros)

# Ordenar las probabilidades de mayor a menor
probabilidades_ordenadas = sorted(probabilidades.items(), key=lambda x: x[1], reverse=True)

# Imprimir las probabilidades ordenadas
print("Probabilidades ordenadas (de mayor a menor):")
for num, prob in probabilidades_ordenadas:
    print(f"Número {num}: {prob*100:.2f}%")
