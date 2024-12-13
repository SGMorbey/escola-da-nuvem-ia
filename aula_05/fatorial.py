#Inicia nossa função
def calcular_fatorial(n):
    """
    Calcula o fatorial de um número inteiro N (0 < N < 13)
    """
    fatorial = 1

#Cria as regras do número fatorial   
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

#Cria a função principal
def main():
    try:
        # Ler o valor de entrada
        N = int(input("Digite um valor inteiro (0 < N < 13): "))

        # Validar o intervalo
        if N <= 0 or N >= 13:
            raise ValueError("O número deve estar entre 1 e 12.")

        # Calcular e exibir o fatorial
        resultado = calcular_fatorial(N)
        print(f"O fatorial de {N} é: {resultado}")

    except ValueError as ve:
        print(f"Erro: {ve}")

if __name__ == "__main__":
    main()
