FRETE_FIXO = 15.0
FRETE_GRATIS_A_PARTIR_DE = 200.0

def total_carrinho(itens):
    total = 0
    for preco, quantidade in itens:
        total = total + preco * quantidade
    return total

def frete(valor_da_compra):
    if valor_da_compra >= FRETE_GRATIS_A_PARTIR_DE:
        return 0.0
    return FRETE_FIXO