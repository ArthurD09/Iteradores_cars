''''
for i in range(11):
    print(i)
'''
class fibonancci:
    def __init__(self, maximo=1000000):
        self.elementoAtual, self.proximoElemento = 0, 1
        self.maximo = maximo
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.elementoAtual > self.maximo:
            raise StopIteration
        
        valorRetorno = self.elementoAtual
        self.elementoAtual, self.proximoElemento = self.proximoElemento, self.elementoAtual + self.proximoElemento

        return valorRetorno

fib = fibonancci()
for numero in fib:
    print(numero)
