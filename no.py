class no:
    def __init__(self, num):
        self.valor = num
        self.esquerda = None
        self.direita = None
        self.Altura = 1

class Arvore:
    def Altura(self, no):
        if no is None:
            return 0
        else:
            return no.Altura

    def Balanceado(self, no):
        
        if no is None:
            return 0
        else:
            return self.Altura(no.esquerda) - self.Altura(no.direita)

    def RotacaoDireita(self, no):
        
        a = no.esquerda
        b = a.direita
        
        a.direita = no
        no.esquerda = b
       
        no.Altura = 1 + max(self.Altura(no.esquerda), self.Altura(no.direita))
        a.Altura = 1 + max(self.Altura(a.esquerda), self.Altura(a.direita))
        return a

    def RotacaoEsquerda(self, no):
        
        a = no.direita
        b = a.esquerda
        
        a.esquerda = no
        no.direita = b

        no.Altura = 1 + max(self.Altura(no.esquerda), self.Altura(no.direita))
        a.Altura = 1 + max(self.Altura(a.esquerda), self.Altura(a.direita))
        return a

    def Inserir(self, val, raiz):

        if raiz is None:
            return no(val)

        elif val <= raiz.valor:

            raiz.esquerda = self.Inserir(val, raiz.esquerda)

        elif val > raiz.valor:
            
            raiz.direita = self.Inserir(val, raiz.direita)

        raiz.Altura = 1 + max(self.Altura(raiz.esquerda), self.Altura(raiz.direita))
        
        Balanceado = self.Balanceado(raiz)
        
        if Balanceado > 1 and raiz.esquerda.valor > val:
            
            return self.RotacaoDireita(raiz)
        
        if Balanceado < -1 and val > raiz.direita.valor:
            
            return self.RotacaoEsquerda(raiz)
       
        if Balanceado > 1 and val > raiz.esquerda.valor:
           
            raiz.esquerda = self.RotacaoEsquerda(raiz.esquerda)
            
            return self.RotacaoDireita(raiz)

        if Balanceado < -1 and val < raiz.direita.valor:
            
            raiz.direita = self.RotacaoDireita(raiz.direita)

            return self.RotacaoEsquerda(raiz)
        return raiz

    def InOrder(self, raiz):

        if raiz is None:
            return
        self.InOrder(raiz.esquerda)
        print(raiz.valor)
        self.InOrder(raiz.direita)

    def PreOrder(self, raiz):
        
        if raiz is None:
            return
        print(raiz.valor)
        self.PreOrder(raiz.esquerda)
        self.PreOrder(raiz.direita)

    def PosOrder(self, raiz):
        
        if raiz is None:
            return
        self.PosOrder(raiz.esquerda)
        self.PosOrder(raiz.direita)
        print(raiz.valor)

Arvore = Arvore()

R = None
R = Arvore.Inserir(3, R)
R = Arvore.Inserir(5, R)
R = Arvore.Inserir(7, R)
R = Arvore.Inserir(2, R)
R = Arvore.Inserir(4, R)
R = Arvore.Inserir(6, R)
R = Arvore.Inserir(8, R)

print("---InOrder---")
Arvore.InOrder(R)
print("---PreOrder")
Arvore.PreOrder(R)
print("---PosOrder")
Arvore.PosOrder(R)