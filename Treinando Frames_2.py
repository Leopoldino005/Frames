from tkinter import *

root = Tk()
root.title('App do Leopoldino 2')

janela_principal = Frame(root, bg = '#483D8B')
janela_principal.place(x = 0, y = 0, relwidth = 1, relheight = 1)

txt_1 = Label(root, text = 'Clique no botão:',fg = 'white', bg = '#483D8B')
txt_1.pack()

b1 = Button(root, text = 'Pressione')
b1.pack()

root.geometry('640x480')
root.mainloop()