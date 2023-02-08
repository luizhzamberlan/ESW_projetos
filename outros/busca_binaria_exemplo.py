from random import randint

def pesquisa_binaria(number_list, left, right, item_buscado):
    #number_list a lista de números que sera buscada um valor específica
    #left o menor valor no ínicio da lista
    #right o maior valor no fim da lista
    #item_buscado o valor a ser buscado dentro da lista

    #1° - Caso a lista seja nula:
    if right < left:
        return -1
        #caso o valor da lista seja nulo, o valor da direita menor que o da esquerda
    
    meio = (right + left)//2

    #2° - Caso a nossa primeira busca localize o item desejado
    if number_list[meio] == item_buscado:
        return meio
    
    #3° - Caso a 1° busca falhe
    elif number_list[meio] > item_buscado:
        return pesquisa_binaria(number_list, left, meio -1, item_buscado)
    
    else: #number_list[meio]<item
        return pesquisa_binaria(number_list, meio + 1, right, item_buscado) 



serie_numeros = [1,0,3,5,4,2,7,6,9,10,8,14,11,18,12,13,19,20,15,17,16]
lista_numeros = sorted(serie_numeros)
numero_sorteado = randint(0,len(lista_numeros)-1)


print(serie_numeros, type(serie_numeros))
print(lista_numeros, type(lista_numeros))
print(numero_sorteado, type(numero_sorteado))

pesquisa = pesquisa_binaria(lista_numeros, 0, len(lista_numeros)-1, numero_sorteado)
#pesquisa = pesquisa_binaria(lista_numeros, 0, len(lista_numeros)-1, 21) -> Pesquisa falha
if pesquisa > -1:
    print("Pesquisa realizada")
else:
    print("Número não encontrado, pesquisa falha")
