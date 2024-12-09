def contagem_i_j():
    i, j = 1, 60  # Valores iniciais
    while j >= 0:  # Condição para continuar o loop
        print(f"I={i} J={j}")
        i += 3  # Incremento de I
        j -= 5  # Decremento de J

# Chamando a função
contagem_i_j()