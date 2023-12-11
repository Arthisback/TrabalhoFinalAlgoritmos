class Tarefa: # Representa a classe e seus atributos
     def __init__(self):
          self.desc = None
          self.limitTime = None
          self.situation = None
          self.status = None
          
     def __str__(self): # Como as instâncias  devem ser representas nos prints
          if self.status == 'A':
               return f"Tarefa: {self.desc} \nTempo limite: {self.limitTime} \nSituação: {self.situation}"
          else:
               None
     
     @staticmethod
     def orderTask(task_list): #Metodo estático para fazer a ordenação das tarefas na função de visualizar tarefas
          ActiveList= []
          ConcluiedList = []
          FinalList = []
          OrderedList = sorted(task_list, key=lambda task:task.limitTime)
          for i in range(len(OrderedList)):
               if OrderedList[i].situation == 'Ativa':
                    ActiveList.append(OrderedList[i])
               elif OrderedList[i].situation == 'Concluido':
                    ConcluiedList.append(OrderedList[i])
          FinalList = ActiveList + ConcluiedList
          return FinalList
# A função sorted funciona da seguinte forma: Ela vai receber o vetor com todas as tarefas e vai ordenar elas de acordo com o atributo tempo limite e após isso a lista vai ser 
# percorrida em um loop para separar em 2 listas onde uma fica as tarefas ativas e na outra as concluidas, no final as 2 listas são juntas
def addTask(task_list): #Função para adicionar tarefas.
     task = Tarefa()
     task.desc = input("Digite a descrição da tarefa: ")
     task.limitTime = input("Digite o tempo limite da tarefa(em horas): ")
     task.situation = 'Ativa'
     task.status = 'A'
     task_list.append(task)
     print(f"Tarefa criada com o ID: {len(task_list)}")

def showTask(task_list): #Função parar mostrar as tarefas que foram adicionadas, pode ser executa de 3 formas, mostrando todas as tarefas(usa do metodo orderTask), mostrar somente as ativas ou entao somente as concluidas
     auxList= Tarefa.orderTask(task_list[:])
     
     print("Para visualizar todas as tarefas digite 1")
     print("Para visualizar as tarefas ativas digite 2")
     print("Para visualizar as tarefas concluidas digite 3")
     option=input()
     if option=="1":
          for i in range(len(auxList)):
               print(auxList[i])
     elif option=="2":
          for i in range(len(auxList)):
               if task_list[i].situation =='Ativa':
                    print(f"Tarefa(s) Ativa(s):{auxList[i]}")
     elif option== "3":
          for i in range(len(task_list)):
               if task_list[i].situation =='Concluido':
                    print(f"Tarefa(s) Concluida(s):{task_list[i]}")
          
def modifyTask(task_list): #Função para alterar os dados de uma tarefa ja adicionada
      for i in range(len(task_list)):
          print(f"Deseja alterar a tarefa com o ID: {i}, 1 para sim ,0 para não")
          option= input()
          if option == "0":
               continue
          elif option =="1":
                task_list[i].desc = input("Digite a descrição da tarefa: ")
                task_list[i].limitTime = input("Digite o tempo limite da tarefa(em horas): ")

def concludeTask(task_list): #Função que muda a sitação de uma tarefa de Ativa pra Concluida
    for i in range(len(task_list)):
          print(f"Deseja concluir a tarefa com o ID: {i}, 1 para sim ,0 para não")
          option= input()
          if option == "0":
               continue
          elif option =="1":
              task_list[i].situation = 'Concluido'
def deleteTask(task_list): #Função que deleta uma tarefa
    for i in range(len(task_list)):
          print(f"Deseja excluir a tarefa com o ID: {i}, 1 para sim ,0 para não")
          option= input()
          if option == "1":
               task_list[i].status = 'I'
               print("Excluido com sucesso!")
          else:
               continue
     

def mainMenu(): #Menu principal onde o usuario pode escolher qual opção ele quer fazer
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
          elif option == "3":
               modifyTask(task_list)
          elif option == "4":
               concludeTask(task_list)
          elif option == "5":
               deleteTask(task_list)
mainMenu()