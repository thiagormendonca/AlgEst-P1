class Arvore:
    raiz = None
class Node:
    valor = None
    esquerda = None
    direita = None
    def __init__(self,valor):
        self.valor = valor

def constroi_arvore(s,p):
    a = Arvore()
    if len(p) == 0:
        return a
    if len(p) == 1:
        a.raiz = Node(p[0])
        return a
    if len(p) == 2:
        a.raiz = Node(p[0])
        a.raiz.esquerda = Node(p[1])
        return a
    if len(p) == 3:
        a.raiz = Node(p[0])
        a.raiz.esquerda = Node(p[1])
        a.raiz.direita = Node(p[2])
        return a
    a.raiz = Node(p[0])
    sraiz = s.index(p[0])
    sesquerda = s[:sraiz]
    sdireita = s[sraiz + 1:]
    pesquerda = ""
    pdireita = ""
    for i in p[1:]:
        if i in sesquerda:
            pesquerda = pesquerda + i
        else:
            pdireita = pdireita + i
    a.raiz.esquerda = constroi_arvore(sesquerda, pesquerda).raiz
    a.raiz.direita = constroi_arvore(sdireita, pdireita).raiz
    return a

def pos_ordem(node):
    if node == None:
        return ""
    if node.esquerda != None:
        return pos_ordem(node.esquerda) + pos_ordem(node.direita) + node.valor
    if node.direita != None:
        return pos_ordem(node.direita) + node.valor
    return node.valor

print(pos_ordem(constroi_arvore("edfbahgic","abdefcghi").raiz))
    