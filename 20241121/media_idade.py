#Função que calcula as idades

def calcular_media_idades():

    """
    Calcula a média de idades de um grupo de indivíduos.
    A leitura termina quando uma idade negativa é inserida.
    """
    
    soma_idades = 0
    quantidade = 0

    while True:
        try:
            # Ler a idade do usuário
            idade = int(input("Digite a idade (número negativo para encerrar): "))

            # Verificar condição de parada
            if idade < 0:
                break

            # Somar idades e contar quantidade
            soma_idades += idade
            quantidade += 1

        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

    # Calcular e exibir a média
    if quantidade > 0:
        media = soma_idades / quantidade
        print(f"A idade média é: {media:.2f}")
    else:
        print("Nenhuma idade válida foi inserida.")

if __name__ == "__main__":
    calcular_media_idades()
