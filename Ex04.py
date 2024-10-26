def busca_binaria(arr, x):
    low = 0
    high = len(arr) - 1
    passos = 0

    while low <= high:
        passos += 1
        mid = (low + high) // 2
        if arr[mid] == x:
            return passos
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

array_ordenado = [2, 4, 6, 8, 10, 12, 13]
numero_a_buscar = 8
passos_binarios = busca_binaria(array_ordenado, numero_a_buscar)
print(f"Número de passos para encontrar a carta N° {numero_a_buscar} com busca binária: {passos_binarios} {'passo' if passos_binarios == 1 else 'passos'}")