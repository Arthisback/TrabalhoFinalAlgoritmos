class Tarefa:
        id = None
        desc = None
        limitTime = None
        situation = None

def addTask(task_list):
     task = Tarefa()
     task.id = input("Digite o ID da tarefa: ")
     task.desc = input("Digite a descrição da tarefa: ")
     task.limitTime = input("Digite o tempo limite da tarefa(em horas): ")
     task.situation = True

#def checkTask(task_list, id):
def showTask(task_list):
     print(task_list)
     
     
def mainMenu():
        task_list= []
        while True:
         print("==========================================")
         print("   Sistema de gerenciamento de tarefas")
         print("==========================================")
         print("Insira a opção desejada! ")
         print("Para sair do programa digite: 0 ")
         print("Para Adicionar tarefa digite: 1 ")
         print("Para Visualizar tarefa digite: 2 ")
         print("Para Alterar uma tarefa digite: 3")
         print("Para Concluir uma tarefa digite: 4")
         print("Para Excluir  uma tarefa digite: 5")
         option = input()
         if option == "0":
            break
         if option == "1":
              addTask(task_list)
         elif option == "2":
                showTask(task_list)
