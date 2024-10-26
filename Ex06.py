def encontrar_quadrado_para_graos(graos):
    quadrado = 1
    graos_atuais = 1

    while graos_atuais < graos:
        quadrado += 1
        graos_atuais *= 2

    return quadrado

graos = 16
print(f"Para {graos} grãos, você precisará do quadrado {encontrar_quadrado_para_graos(graos)}.")

# Explicação da Notação Big O
# A complexidade de tempo da função é O(1) - tempo constante, porque o cálculo do logaritmo é feito de forma bem rápida e independe da quantidade.
# Então, não importa quantos grãos você tenha, o tempo pra calcular vai ser quase sempre o mesmo, o que faz a função ser bem eficiente.