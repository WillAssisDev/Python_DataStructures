class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None


class Fila:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def vazia(self):
        return True if not self._quantidade else False

    def entrar(self, conteudo):
        nova_celula = Celula(conteudo)
        if not self._quantidade:
            self._inicio = nova_celula
            self._fim = nova_celula
        else:
            nova_celula.anterior = self._fim
            self._fim.proximo = nova_celula
            self._fim = nova_celula
        self._quantidade += 1

    def sair(self):
        if self._quantidade:
            if self._quantidade == 1:
                removido = self._inicio
                self._inicio = None
                self._fim = None
            else:
                removido = self._inicio
                direita = removido.proximo
                self._inicio = direita
                self._inicio.anterior = None
            removido.proximo = None
            removido.anterior = None
            self._quantidade -= 1
            return removido.conteudo
        else:
            raise IndexError('Lista vazia.')

    def imprimir(self):
        atual = self._inicio
        for celula in range(0, self._quantidade):
            print(atual.conteudo)
            atual = atual.proximo
        print()
