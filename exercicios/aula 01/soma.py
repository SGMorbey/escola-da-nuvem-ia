# Função para obter um número inteiro com validação
def leia_inteiro():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Leia dois valores inteiros com validação
A = leia_inteiro()
B = leia_inteiro()

# Calcule a soma
SOMA = A + B

# Exiba o resultado no formato especificado
print(f"SOMA = {SOMA}")