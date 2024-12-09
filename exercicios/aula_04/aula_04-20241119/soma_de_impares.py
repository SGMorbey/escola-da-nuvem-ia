try:
    n = int(input("Digite o número de casos de teste: "))
except ValueError:
    print("Erro: Por favor, insira um número inteiro válido.")
    exit()

for _ in range(n):
    try:
        x, y = map(int, input("Digite dois números separados por espaço: ").split())
        if x > y:
            x, y = y, x

        soma = sum(i for i in range(x + 1, y) if i % 2 != 0)
        print(soma)
    except ValueError:
        print("Erro: Por favor, insira dois números inteiros válidos.")
