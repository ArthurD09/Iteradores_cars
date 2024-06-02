def fibonacci(maximo):
    elementoAtual, proximoElemento = 0 , 1 

    while elementoAtual < maximo:
        yield elementoAtual

 
        elementoAtual, proximoElemento = proximoElemento, elementoAtual + proximoElemento
'''     0                   0               0                   0                   0       = 0 
        0                   1               1                   0                   1       = 1
        1                   1               1                   1                   1       = 2
        1                   2               2                   1                   2       = 3
        2                   3               3                   2                   3       = 5
        3                   5               5                   3                   5       = 8
'''

fib = fibonacci(1000000)
for i in fib:
    print(i)