TAMANHOS = ("PP", "P", "M", "G", "GG")

class Produto:
    def __init__(self, nome, preco, tamanho):
        if not nome or not nome.strip():
            raise ValueError("Nome do produto não pode ser vazio!")
        if preco <= 0:
            raise ValueError("O preço precisa ser maior que 0!")
        if tamanho not in TAMANHOS:
            raise ValueError(f"Tamanho inválido: {tamanho}")

        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho

    def descricao(self):
        return f"{self.nome} {self.tamanho} : R${self.preco:.2f}"