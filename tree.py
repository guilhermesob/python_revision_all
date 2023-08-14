class NoArvore:
def __init__(self, chave = None, esquerda = None, direita = None):
     self.chave = chave
     self.esquerda = esquerda
     self.direita = direita

if __name__ == '__main__':
   raiz = NoArvore(6)
   raiz.esquerda = NoArvore(8)
   raiz.direita = NoArvore(4)
