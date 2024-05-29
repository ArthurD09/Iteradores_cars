def fibonacci(maximo):
    elementoAtual, proximoElemento = 0 , 1 

    while elementoAtual < maximo:
        yield elementoAtual

 
        elementoAtual, proximoElemento = proximoElemento, elementoAtual + proximoElemento

fib = fibonacci(1000000)
for i in fib:
    print(i)