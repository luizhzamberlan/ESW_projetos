numero_binario = list(input('falae: '))

tamanho = len(numero_binario) - 1
indice = 0
conversao_p_dec = 0


for i in range(tamanho, -1, -1):
    conversao_p_dec += int(numero_binario[indice]) * (2 ** i)
    indice += 1

print(conversao_p_dec)
