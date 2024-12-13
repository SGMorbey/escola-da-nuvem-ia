#Esse código verifica a idade se é maior de idade, se é adolescente ou se é uma criança.

idade = int(input("Digite a sua idade: "))

#Se a idade da pessoa for maior que 18 anos ela é maior de idade
if idade >= 18:
    print("Você é maior de idade")
#Se a idade da pessoa for maior ou igual a 12 anos e menor que 18 anos ela é adolescente
elif 12 <= idade < 18:
    print("Você é adolescente")
#Se não for nenhuma dessas é uma criança
else:
    print("Você é uma criança")
