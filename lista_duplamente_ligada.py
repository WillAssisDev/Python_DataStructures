class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None
        self.anterior = None


class ListaDuplamenteLigada:

    def __init__(self):
        self._inicio = None
        self._fim = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def fim(self):
        return self._fim

    @property
    def quantidade(self):
        return self._quantidade

    def _validar_posicao(self, posicao):
        if 0 <= posicao < self.quantidade:
            return True
        else:
            raise IndexError(f'Posição {posicao} inválida.')

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        metade = self.quantidade // 2
        if posicao <= metade:
            atual = self.inicio
            for celula in range(0, posicao):
                atual = atual.proximo
        else:
            atual = self.fim
            for celula in range(self.quantidade - 1, posicao, -1):
                atual = atual.anterior
        return atual

    def inserir(self, conteudo, posicao=None, inicio=True):
        nova_celula = Celula(conteudo)
        if not self.quantidade: # lista vazia
            self._inicio = nova_celula
            self._fim = nova_celula
        elif inicio and not posicao: # inserir no inicio
            nova_celula.proximo = self._inicio
            self._inicio.anterior = nova_celula
            self._inicio = nova_celula
        elif (not inicio and not posicao) or posicao == self.quantidade: # inserir no fim
            nova_celula.anterior = self._fim
            self._fim.proximo = nova_celula
            self._fim = nova_celula
        elif posicao: # inserir em posição definida
            esquerda = self._celula(posicao - 1)
            direita = esquerda.proximo
            nova_celula.proximo = direita
            nova_celula.anterior = esquerda
            esquerda.proximo = nova_celula
            direita.anterior = nova_celula
        self._quantidade += 1

    def remover(self, posicao=None, inicio=True):
        if self.quantidade:
            if self.quantidade == 1: # último item
                removido = self._inicio
                self._inicio = None
                self._fim = None
            elif inicio and not posicao: # remover do inicio
                removido = self._inicio
                direita = removido.proximo
                self._inicio = direita
                self._inicio.anterior = None
            elif (not inicio and not posicao) or posicao == self.quantidade - 1: # remover do fim
                removido = self._fim
                esquerda = removido.anterior
                self._fim = esquerda
                self._fim.proximo = None
            elif posicao: # remover posição definida
                removido = self._celula(posicao)
                esquerda = removido.anterior
                direita = removido.proximo
                esquerda.proximo = direita
                direita.anterior = esquerda
            removido.proximo = None
            removido.anterior = None
            self._quantidade -= 1
            return removido.conteudo
        else:
            raise IndexError('Lista vazia.')

    def item(self, posicao):
        return self._celula(posicao).conteudo

    def imprimir(self, inicio=True):
        if inicio:
            atual = self.inicio
            for celula in range(0, self.quantidade):
                print(atual.conteudo)
                atual = atual.proximo
        else:
            atual = self.fim
            for celula in range(self.quantidade, 0, -1):
                print(atual.conteudo)
                atual = atual.anterior
        print()
