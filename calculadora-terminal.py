from calculadora import Calculadora
import os

def main():
     os.system('cls')
     cabecalho()
     opcoes()

def cabecalho():
    print('''
------------------------------------------------------      
____ ____ _    ____ _  _ _    ____ ___  ____ ____ ____ 
|    |__| |    |    |  | |    |__| |  \ |  | |__/ |__| 
|___ |  | |___ |___ |__| |___ |  | |__/ |__| |  \ |  |
------------------------------------------------------                                                 
    ''')

def opcoes():
     print('1 - ACESSAR A CALCULADORA\n2 - SAIR DA APLICAÇÃO\n')
     opcao_desejada = int(input('Escolha uma das opções listadas acima: '))
     if opcao_desejada == 1:
          calculo()
     elif opcao_desejada == 2:
          os.system('cls')
          print('Finalizando Aplicação...')
          os.system('exit')
     else: 
          input('Esta é uma opção inválida, por favor, digite qualquer tecla para tentar novamente ')
          main()

def calculo():
    os.system('cls')
    cabecalho()
    calculo = Calculadora(input('Digite a conta: ').split(' '))

    lista_componentes = calculo._memoria

    while len(lista_componentes) != 1:
            if '*' in lista_componentes:
                calculo.multiplicar(lista_componentes[lista_componentes.index('*')-1], lista_componentes[lista_componentes.index('*')+1])
            elif '/' in lista_componentes:
                calculo.dividir(lista_componentes[lista_componentes.index('/')-1], lista_componentes[lista_componentes.index('/')+1])
            elif '+' in lista_componentes:
                calculo.somar(lista_componentes[lista_componentes.index('+')-1], lista_componentes[lista_componentes.index('+')+1])
            else:
                calculo.dividir(lista_componentes[lista_componentes.index('-')-1], lista_componentes[lista_componentes.index('-')+1])

    print(f'RESULTADO --> {calculo._memoria[0]}')

    input('Digite qualquer tecla para voltar ao menu')
    main()

if __name__ == '__main__':
    main()

