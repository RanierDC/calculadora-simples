from tkinter import *
from tkinter import ttk

root = Tk()

class Aplicacao():
    def __init__(self):
        self.root = root
        self.valor_texto = StringVar()
        self.todos_valores = ''
        self.tela()
        root.mainloop()

    def tela(self):
        # Título do aplicativo
        self.root.title('Calculadora')
        # onfigurações do app
        self.root.geometry('225x325')
        self.root.wm_resizable(False, False)
        self.frames_tela()

    def frames_tela(self):
        self.frame_conta = Frame(self.root, width=250, height=60, background='#198ca6')
        self.frame_conta.grid(row=0, column=0)

        self.frame_botoes = Frame(self.root, width=250, height=265, background='#8ddef0')
        self.frame_botoes.grid(row=1, column=0)

        self.botoes_tela()
        self.label_tela()

    def botoes_tela(self):
        self.botao_limpar = Button(self.frame_botoes, command = lambda: self.limpar_tela(), text='C', width=13, height=2)
        self.botao_limpar.place(x=10, y=0)

        self.botao_ = Button(self.frame_botoes, command = lambda: self.entrar_valor('%'), text='%', width=6, height=2)
        self.botao_.place(x=108, y=0)

        self.botao_dividir = Button(self.frame_botoes, command = lambda: self.entrar_valor('/'), text='/', width=6, height=2, background='#c72235')
        self.botao_dividir.place(x=163, y=0)

        self.botao_numero7 = Button(self.frame_botoes, command = lambda: self.entrar_valor('7'), text='7', width=6, height=2)
        self.botao_numero7.place(x=10, y=42)

        self.botao_numero8 = Button(self.frame_botoes, command = lambda: self.entrar_valor('8'), text='8', width=6, height=2)
        self.botao_numero8.place(x=58, y=42)

        self.botao_numero9 = Button(self.frame_botoes, command = lambda: self.entrar_valor('9'), text='9', width=6, height=2)
        self.botao_numero9.place(x=108, y=42)
        
        self.botao_multiplicar = Button(self.frame_botoes, command = lambda: self.entrar_valor('*'), text='*', width=6, height=2, background='#c72235')
        self.botao_multiplicar.place(x=163, y=42)

        self.botao_numero4 = Button(self.frame_botoes, command = lambda: self.entrar_valor('4'), text='4', width=6, height=2)
        self.botao_numero4.place(x=10, y=84)

        self.botao_numero5 = Button(self.frame_botoes, command = lambda: self.entrar_valor('5'), text='5', width=6, height=2)
        self.botao_numero5.place(x=58, y=84)

        self.botao_numero6 = Button(self.frame_botoes, command = lambda: self.entrar_valor('6'), text='6', width=6, height=2)
        self.botao_numero6.place(x=108, y=84)

        self.botao_subtrair = Button(self.frame_botoes, command = lambda: self.entrar_valor('-'), text='-', width=6, height=2, background='#c72235')
        self.botao_subtrair.place(x=163, y=84)
        
        self.botao_numero1 = Button(self.frame_botoes, command = lambda: self.entrar_valor('1'), text='1', width=6, height=2)
        self.botao_numero1.place(x=10, y=126)

        self.botao_numero2 = Button(self.frame_botoes, command = lambda: self.entrar_valor('2'), text='2', width=6, height=2)
        self.botao_numero2.place(x=58, y=126)

        self.botao_numero3 = Button(self.frame_botoes, command = lambda: self.entrar_valor('3'), text='3', width=6, height=2)
        self.botao_numero3.place(x=108, y=126)

        self.botao_somar = Button(self.frame_botoes, command = lambda: self.entrar_valor('+'), text='+', width=6, height=2, background='#c72235')
        self.botao_somar.place(x=163, y=126)
    
        self.botao_numero0 = Button(self.frame_botoes, command = lambda: self.entrar_valor('0'), text='0', width=13, height=2)
        self.botao_numero0.place(x=10, y=168)

        self.botao_decimal = Button(self.frame_botoes, command = lambda: self.entrar_valor('.'), text='.', width=6, height=2)
        self.botao_decimal.place(x=108, y=168)

        self.botao_igual = Button(self.frame_botoes, command = lambda: self.calcular(), text='=', width=6, height=2, background='#c72235')
        self.botao_igual.place(x=163, y=168)

    def label_tela(self):
        self.app_label = Label(self.frame_conta, textvariable=self.valor_texto, width=14, height=2, padx=7, relief="flat", anchor="e", bd=10, justify=CENTER, font=('Ivy 18'), bg='#37474F', fg='white')
        self.app_label.place(x=0, y=0)

    def entrar_valor(self, event):
        self.todos_valores = self.todos_valores + str(event)
        self.valor_texto.set(self.todos_valores)

    def calcular(self):
        resultado = str(round(eval(self.todos_valores),2))
        self.valor_texto.set(resultado)
        self.todos_valores = ""

    def limpar_tela(self): 
        self.todos_valores = ''
        self.valor_texto.set('')
    

Aplicacao()

