def fibonacci(n):
    """
    Gerar os N primeiros números da série de Fibonacci
    """
    # Iniciar os primeiros valores da série
    a, b = 0, 1
    resultado = [a]

    # Geração dos termos
    for i in range(1, n):
        resultado.append(b)
        a, b = b, a + b

    return resultado

def main():
    try:
        # Ler o valor de entrada
        N = int(input("Digite um valor inteiro (0 < N < 46): "))

        # Validar se N está no intervalo permitido
        if N <= 0 or N >= 46:
            raise ValueError("O número precisa estar entre 1 e 45")

        # Gerar e imprimir os N primeiros números da série de Fibonacci
        fibonacci_sequence = fibonacci(N)
        print(" ".join(map(str, fibonacci_sequence)))

    except ValueError as ve:
        print(f"Erro: {ve}")

if __name__ == "__main__":
    main()
