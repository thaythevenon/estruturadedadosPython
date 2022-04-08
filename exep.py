class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __str__(self):
        return str(self.dado)
# Implementacao Pilha baseada na List do Python
class Pilhas:
    def __init__(self):
        self.pilha = ["azul","verde","amarelo"] # lista interna
    def push(self, item): # metodo de inserir item
        item = "vermelho"
        self.pilha.append(item)
        print("Inserindo um item na lista",self.pilha)
    def peek(self): # retorna qual item esta no topo
        print("O segundo item na lista é:",self.pilha[1])
    def pop(self): # remover o topo e retornar item para usuario
        self.pilha.pop()
        print("Removendo o ultimo item na lista",self.pilha)
                
    def __len__(self): # retorna o total de itens
        print("O tamanho da lista é:",len(self.pilha))
        
    

    
pilha = Pilhas()
pilha.push(Nodo)
pilha.peek()
pilha.pop()
pilha.__len__()