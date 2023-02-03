# input para receber os números em binário
numero_binario = list(input('Digite o número binário: '))

tamanho_da_lista = len(numero_binario) - 1
indice = 0
conversao_p_dec = 0

# cálculo para conversão de base_binária
for i in range(tamanho, -1, -1):
    conversao_p_dec += int(numero_binario[indice]) * (2 ** i)
    indice += 1

print(conversao_p_dec)
