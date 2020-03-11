class Celula:

    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None


class ListaLigada:

    def __init__(self):
        self._inicio = None
        self._quantidade = 0

    @property
    def inicio(self):
        return self._inicio

    @property
    def quantidade(self):
        return self._quantidade

    def _validar_posicao(self, posicao):
        if 0 <= posicao <= self.quantidade:
            return True
        else:
            raise IndexError(f'Posição {posicao} inválida')

    def _celula(self, posicao):
        self._validar_posicao(posicao)
        atual = self.inicio
        for elemento in range(0, posicao):
            atual = atual.proximo
        return atual

    def inserir(self, conteudo, posicao=None):
        nova_celula = Celula(conteudo)
        if not posicao:
            nova_celula.proximo = self._inicio
            self._inicio = nova_celula
        else:
            esquerda = self._celula(posicao - 1)
            nova_celula.proximo = esquerda.proximo
            esquerda.proximo = nova_celula
        self._quantidade += 1

    def remover(self, posicao=None):
        if not posicao:
            removido = self._inicio
            self._inicio = removido.proximo
        else:
            esquerda = self._celula(posicao)
            removido = esquerda.proximo
            esquerda.proximo = removido.proximo
        removido.proximo = None
        self._quantidade -= 1
        return removido.conteudo

    def item(self, posicao):
        return self._celula(posicao).conteudo

    def imprimir(self):
        atual = self.inicio
        for elemento in range(0, self.quantidade):
            print(atual.conteudo)
            atual = atual.proximo
