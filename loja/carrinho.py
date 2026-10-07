from .calculos import frete, total_carrinho
from .produto import Produto
from .promocao import SemPromocao


class Carrinho:
    def __init__(self, promocao=None):
        self._itens = []
        self._finalizado = False
        self.promocao = promocao or SemPromocao()


    def adicionar(self, produto, quantidade = 1):
        if self._finalizado:
            raise CarrinhoFinalizadoError("Carrinho finalizado não recebe peças!")
        if not isinstance(produto, Produto):
            raise TypeError("Só é possível adicionar um produto!")
        if quantidade <= 0:
            raise ValueError("A Quantidade deve ser positiva!")

        self._itens.append((produto, quantidade))

    @property
    def itens(self):
        return list(self._itens)

    @property
    def quantidade_de_pecas(self):
        return sum(quantidade for _, quantidade in self._itens)

    @property
    def subtotal(self):
        return total_carrinho([(p.preco, q) for p, q in self._itens])

    @property
    def total(self):
        return self.subtotal + frete(self.subtotal)

    def finalizar(self):
        if not self._itens:
            raise ValueError("Não é possível finalizar um carrinho vazio!")
        self._finalizado = True

    @property
    def total(self):
        com_desconto = self.promocao.aplicar(self.subtotal)
        return self.subtotal + frete(com_desconto)
    