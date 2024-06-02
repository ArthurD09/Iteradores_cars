# 0 1 1 2 3 5 8 13 21

maximo = 10 
atual = 0 
proximo = 1
for numero in range(maximo):
    auxiliar = atual
    print(auxiliar)
    if proximo > maximo:
        break
    atual = proximo
    proximo = auxiliar + proximo
    numero = proximo

print('Fora do for')

valor_string = 'UltimaSchool'
objeto_iter = iter(valor_string)

while True:
    try:
        item = next(objeto_iter)
        print(item)

    except StopIteration:

        break


def fibonacci(maximo):
    elemento_atual = 0 
    proximo_elemento = 1 
    while elemento_atual < maximo:
        yield elemento_atual

        elemento_atual, proximo_elemento = proximo_elemento, elemento_atual = proximo_elemento
