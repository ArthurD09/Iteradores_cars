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
