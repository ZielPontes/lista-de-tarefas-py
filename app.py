import os
lista = []

class Functions:
    def clear(self):
        pass
    def addTask(self):
        pass
    def createList(self):
        pass
    def removeTask(self):
        pass
# chamando a classe:
fc = Functions()
while True:
    # Menu principal
    print('Lista de Tarefas. by: Ziel Pontes')

    print('---------- Menu ----------')
    print('\n1 - Adicionar tarefa. ')
    print('2 - Excluir tarefa. ')
    print('3 - Listar tarefa. ')
    print('4 - Sair tarefa. ')
    print('\n--------------------------')
    chose = input('Insira sua escolha => ')

    # Condicionais para o menu.
    if chose == '1':
        fc.clear()
        fc.addTask()
    elif chose =='2':
        fc.clear()
        fc.removeTask()
    elif chose =='3':
        fc.clear()
        fc.()
    elif chose =='4':
        fc.clear()
        fc.removeTask()