import random

def main():
    # Gerar 100 números aleatórios entre 1 e 10.000
    valor = [random.randint(1, 10000) for _ in range(100)]
    
    # Encontrar o maior valor e sua posição
    maior = max(valor)
    posicao = valor.index(maior) + 1

    # Exibir os resultados
    print("\nNúmeros gerados:")
    print(valor)
    print("\nMaior Valor:", maior)
    print("Posição do Maior Valor:", posicao)

# Invocar a função principal
if __name__ == "__main__":
    main()
