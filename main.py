from collections import deque
import collections
import time
import os

fila = deque([])
for i in range (0,301):
  fila.append(i)

while True:
    os.system("cls")
    
    print("====SENHAS====")
    

    print("| Escolha uma opcao do menu:")
    print("|_ 1 - OBTER NOVA SENHA")
    print("|_ 2 - CHAMAR PROXIMA SENHA")
    print("|_ 3 - MOSTRAR ULTIMA SENHA CHAMADA")
    print("|_ 0- SAIR")
  

    while True:    
        try:
            opcao = int(input())
            if opcao in (0,1,2,3):
                break
            else:
                print("Opção inválida. Digite novamente!")
        except ValueError:
            print("Apenas números são aceitos como opcao!")
    if opcao == 1:
       
     fila.popleft()
     print("A sua senha é",fila[0])
     time.sleep(2)
     os.system("cls") 
        
    elif opcao == 2:
       fila.popleft()
       print("A proxima senha é:",fila[0])
       time.sleep(2)
       os.system("cls")  
    elif opcao == 3:
     #mostrar todas as senhas
      print("A ultima senha chamada foi:", fila[0])
      time.sleep(3)
      os.system("cls")
    elif opcao == 0:
        break # volta para menu anterior