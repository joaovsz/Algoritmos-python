def busca_linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i + 1  
    return -1  

array_ordenado = [2, 4, 6, 8, 10, 12, 13]
numero_a_buscar = 8
passos = busca_linear(array_ordenado, numero_a_buscar)
print(f"Número de passos para encontrar a carta N° {numero_a_buscar}: {passos} passos")
