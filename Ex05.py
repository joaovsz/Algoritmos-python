def maiorNumero(array):
    valor_maximo = float('-inf')    
    for num in array:
        if num > valor_maximo:
            valor_maximo = num
    
    return valor_maximo

array = [3, 5, 7, 2, 8, -1, 4, 10]
print(maiorNumero(array))