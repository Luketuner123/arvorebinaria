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
        
        novo_node = Node(dado=dado,esquerda=None,direita=None)
        
        #Ir para a ESQUERDA da raiz
        atual = self.raiz
        while True:
            if (dado <= self.raiz.dado):

                if (atual.esquerda is None):
                    atual.esquerda = novo_node
                    return False
                
                elif (dado <= atual.esquerda.dado):
                    atual = atual.esquerda
                
                # Condição dado > node --> ir para a direita
                elif (dado > atual.esquerda.dado):
                    
                    if atual.esquerda.direita is None:
                        atual.esquerda.direita = novo_node
                        return False
                    else:
                        atual = atual.esquerda.direita
            
            # Condição para a direita
            else:
                ...


        


if __name__ == '__main__':

    arvore = BST()
    arvore.inserir(50)
    arvore.inserir(30)
    arvore.inserir(40)
    arvore.inserir(49)


    print(arvore.raiz.dado)
    print(arvore.raiz.esquerda.dado)
    print(arvore.raiz.esquerda.direita.dado)
    print(arvore.raiz.esquerda.direita.esquerda)
    # print(arvore.raiz.esquerda.direita.direita.dado)