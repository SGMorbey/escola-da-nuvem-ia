# Tabela de preços
precos = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

# Leia o código do item e a quantidade
codigo, quantidade = map(int, input().split())

# Calcule o valor total
total = precos[codigo] * quantidade

# Mostre o valor total formatado com duas casas decimais
print(f"Total: R$ {total:.2f}")
