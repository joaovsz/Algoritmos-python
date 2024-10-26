import random

def embaralhar_cartas():
    cartas = list(range(1, 14))  
    random.shuffle(cartas)
    return cartas

def ordenar_cartas(cartas):
    mao = []  
    while cartas:
        carta = cartas.pop(0)  
        if not mao:
            mao.append(carta)
        else:
            inserido = False
            for i in range(len(mao)):
                if carta < mao[i]:
                    mao.insert(i, carta)
                    inserido = True
                    break
            if not inserido:
                mao.append(carta)
    return mao



cartas_embaralhadas = embaralhar_cartas()
print("Cartas embaralhadas:", cartas_embaralhadas)
cartas_ordenadas = ordenar_cartas(cartas_embaralhadas)
print("Cartas ordenadas:", cartas_ordenadas)
