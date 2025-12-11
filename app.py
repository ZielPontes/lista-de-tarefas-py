import os
lista = []

class Functions:
    def clear(self):
        os.system('cls' if os.name =='nt' else 'clear' )
    def addTask(self):
        while True:
            print('---------- Adicionar Tarefa ----------')
            task = input('Informe a tarefa.\n(Digite [0] para retornar ao Menu)\n==> ')
            if task == '':
                input('Campo vazio. Por favor, preencha corretamente. [Aperte Enter]')
            elif task =='0':
                return
            else:
                lista.append(task)
                print(f'Tarefa [{task}] adicionada com sucesso!')
                while True:
                    chose = input('\nDeseja adicionar nova tarefa? (s/n) ==> ')
                    fc.clear()
                    if chose =='':
                        fc.clear()
                        print('Campo vazio. Preencha [s] para Sim ou [n] para não.')
                        continue
                    elif chose =='s':
                        break # break encerra o loop continuando dentro da função
                    elif chose=='n':
                        return # return serve para encerrar o loop e a função retornando pra onde ela foi chamada.
                    else:
                        input('Campo inválido. [Aperte Enter]')
    
    def createList(self):
        print('------------ Lista de Tarefas ------------')
        if not lista:
            print('Nenhuma tarefa cadastrada.')
        else:
            for i, task in enumerate(lista, start=1):
                print(f'#{i} - {task}.')
    def listTask(self):
        fc.clear()
        fc.createList()
        input('------------------------------------------\nPressione [Enter] para retornar ao menu.')

    def removeTask(self):
        pass
# chamando a classe:
fc = Functions()
while True:
    fc.clear()
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
        fc.listTask()
    elif chose =='4':
        print('Até a próxima!! :D')
        break