#Vizualizador em http://btv.melezinek.cz/binary-search-tree.html

class Node():

    def __init__(self, dado = None, esquerda = None, direita = None):
        self.dado = dado
        self.esquerda = esquerda
        self.direita = direita


class BST():

    def __init__(self, raiz= None):
        self.raiz = Node(dado=None,esquerda=None,direita=None)

    def inserir(self, dado):

        if self.raiz.dado is None:
            self.raiz.dado = dado
            return True
        
        #Novo node recebe um node com o dado passado pelo usuário
        novo_node = Node(dado=dado,esquerda=None,direita=None)
        
        #Ir para a ESQUERDA da raiz
        node_atual = self.raiz
        while True:
            if (dado <= node_atual.dado):

                if (node_atual.esquerda is None):
                    node_atual.esquerda = novo_node
                    return False
                
                else:
                    node_atual = node_atual.esquerda
            
            else:
                if (node_atual.direita is None):
                    node_atual.direita = novo_node
                    return False
                
                else: 
                    node_atual = node_atual.direita
                

                
           

        


if __name__ == '__main__':

    arvore = BST()
    arvore.inserir(50)
    arvore.inserir(30)
    arvore.inserir(20)
    arvore.inserir(10)
    arvore.inserir(25)
    arvore.inserir(40)


    print(arvore.raiz.dado)
    print(arvore.raiz.esquerda.dado)
    print(arvore.raiz.esquerda.esquerda.dado)
    print(arvore.raiz.esquerda.esquerda.esquerda.dado)
    print(arvore.raiz.esquerda.esquerda.direita.dado)
    print(arvore.raiz.esquerda.direita.dado)



    # print(arvore.raiz.esquerda.direita.esquerda)
    # print(arvore.raiz.esquerda.direita.direita.dado)
