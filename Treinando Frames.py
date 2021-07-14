from tkinter import *       #Importando biblioteca
from time import sleep      # Importando biblioteca

# Classe do Aplicativo
class Cadastro():
    # Atributos
    nome = 'Oooo'
    idade = '18'
    senha = 'xxxxx'

    def menu(self):     # função Menu
        print("Bem-Vindo!")
        print()
        novo_nome = str(input("Informe seu nome: "))
        self.erros(novo_nome)
        self.nome = novo_nome
        print()
        nova_idade = int(input("Informe sua idade: "))
        self.idade = nova_idade
        print()
        nova_senha = int(input("Informe sua senha: "))
        self.senha = nova_senha

    def erros_nome(self, nome):
        try:
            self.nome = str(self.nome)
            return sleep(2), print("Ok")

        except:
            print("O nome digitado é inválido!")
            return 0

pop = Cadastro()

root = Tk()     # Variavél reponsável pelo
root.title("App do leopoldino ")    # Título

root(txt_menu = pop.menu())

root.geometry('640x480')
root.minisize(320,240)
root.mainloop()