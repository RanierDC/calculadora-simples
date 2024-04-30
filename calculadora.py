class Calculadora:
    def __init__(self, memoria):
        self._memoria = memoria

    def somar(self, x, y):
        resultado = int(x) + int(y)
        self._memoria.insert(self._memoria.index(x), f'{resultado}')
        self._memoria.remove(self._memoria[self._memoria.index(x)])
        self._memoria.remove(self._memoria[self._memoria.index('+')])
        self._memoria.remove(self._memoria[self._memoria.index(y)])

    def subtrair(self, x, y):
        resultado = int(x) - int(y)
        self._memoria.insert(self._memoria.index(x), f'{resultado}')
        self._memoria.remove(self._memoria[self._memoria.index(x)])
        self._memoria.remove(self._memoria[self._memoria.index('-')])
        self._memoria.remove(self._memoria[self._memoria.index(y)])

    def multiplicar(self, x, y):
        resultado = int(x) * int(y)
        self._memoria.insert(self._memoria.index(x), f'{resultado}')
        self._memoria.remove(self._memoria[self._memoria.index(x)])
        self._memoria.remove(self._memoria[self._memoria.index('*')])
        self._memoria.remove(self._memoria[self._memoria.index(y)])

    def dividir(self, x, y):
        resultado = int(x) / int(y)
        self._memoria.insert(self._memoria.index(x), f'{resultado}')
        self._memoria.remove(self._memoria[self._memoria.index(x)])
        self._memoria.remove(self._memoria[self._memoria.index('/')])
        self._memoria.remove(self._memoria[self._memoria.index(y)])

    
        
