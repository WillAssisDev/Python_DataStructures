class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None


class Pilha:

    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def topo(self):
        return self._inicio.conteudo

    @property
    def vazia(self):
        return True if not self._quantidade else False

    def empilhar(self, conteudo):
        nova_celula = Celula(conteudo)
        nova_celula.proximo = self._inicio
        self._inicio = nova_celula
        self._quantidade += 1

    def desempilhar(self):
        removido = self._inicio
        self._inicio = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def imprimir(self):
        atual = self._inicio
        for elemento in range(0, self._quantidade):
            print(atual.conteudo)
            atual = atual.proximo
