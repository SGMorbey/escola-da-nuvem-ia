import random

# Definindo as 10 perguntas e suas opções com pesos
perguntas = [
    {"pergunta": "Na escola, você se sente:", "opcoes": [("Triste e sozinho(a) a maior parte do tempo", 1), ("Um pouco triste e com dificuldade para fazer amigos.", 2), ("Nem feliz nem triste, apenas normal.", 3), ("Feliz e com vários amigos.", 4), ("Muito feliz e animado(a) para ir à escola todos os dias.", 5)]},
    {"pergunta": "O que te deixa mais feliz na escola?", "opcoes": [("Nada me deixa feliz na escola.", 1), ("Quando termino as atividades rápido.", 2), ("Quando tenho tempo livre para brincar.", 3), ("Quando estou com meus amigos.", 4), ("Quando aprendo coisas novas e interessantes.", 5)]},
    {"pergunta": "O que te deixa mais triste na escola?", "opcoes": [("Tudo me deixa triste na escola.", 1), ("Quando não entendo as explicações do professor.", 2), ("Quando brigo com meus amigos", 3), ("Raramente fico triste na escola.", 4), ("Nada me deixa triste na escola.", 5)]},
    {"pergunta": "Você tem algum amigo especial na escola?", "opcoes": [("Não tenho nenhum amigo na escola.", 1), ("Tenho poucos amigos e fico sozinho(a) na maioria do tempo.", 2), ("Tenho alguns amigos, mas não muito próximos.", 3), ("Tenho muitos amigos e nos divertimos juntos.", 4), ("Tenho um melhor amigo e somos inseparáveis", 5)]},
    {"pergunta": "Você se sente seguro(a) na escola?", "opcoes": [("Não me sinto seguro(a) de forma alguma.", 1), ("Às vezes me sinto inseguro(a).", 2), ("Me sinto mais ou menos seguro(a).", 3), ("Me sinto bastante seguro(a).", 4), ("Me sinto completamente seguro(a).", 5)]},
    {"pergunta": "Você gosta das atividades que fazemos na escola?", "opcoes": [("Detesto todas as atividades da escola.", 1), ("Não gosto muito das atividades.", 2), ("As atividades são mais ou menos.", 3), ("Gosto de algumas atividades.", 4), ("Amo todas as atividades da escola.", 5)]},
    {"pergunta": "Se pudesse mudar uma coisa na escola, o que seria?", "opcoes": [("Mudaria tudo na escola.", 1), ("Gostaria que as aulas fossem mais curtas.", 2), ("Gostaria de ter mais tempo livre.", 3), ("Gostaria de ter mais atividades divertidas.", 4), ("Não mudaria nada na escola.", 5)]},
    {"pergunta": "Você se sente sozinho(a) na escola?", "opcoes": [("Sim, me sinto muito sozinho(a).", 1), ("Sim, às vezes me sinto sozinho(a).", 2), ("As vezes me sinto sozinho(a), mas tenho meus momentos.", 3), ("Raramente me sinto sozinho(a).", 4), ("Nunca me sinto sozinho(a) na escola.", 5)]},
    {"pergunta": "Você tem alguma matéria que te dá muito trabalho?", "opcoes": [("Todas as matérias são muito difíceis.", 1), ("Tenho dificuldade em algumas matérias.", 2), ("As matérias são mais ou menos.", 3), ("Tenho facilidade com a maioria das matérias.", 4), ("Todas as matérias são fáceis para mim.", 5)]},
    {"pergunta": "Se pudesse descrever a escola com uma palavra, qual seria?", "opcoes": [("Terrível.", 1), ("Chata.", 2), ("Normal.", 3), ("Divertida.", 4), ("Maravilhosa.", 5)]}
]

# Sorteando 5 perguntas aleatórias
perguntas_selecionadas = random.sample(perguntas, 5)

# Coletando respostas do usuário
respostas = []

for i, pergunta in enumerate(perguntas_selecionadas):
    print(f"{i+1}. {pergunta['pergunta']}")
    for j, opcao in enumerate(pergunta["opcoes"]):
        print(f"   {j+1}. {opcao[0]}")
    
    while True:
        try:
            resposta = int(input("Selecione uma opção (1-5): ")) - 1
            if 0 <= resposta < 5:
                respostas.append(resposta)
                break
            else:
                print("Entrada inválida. Por favor, selecione um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Calculando a média dos pesos das respostas
total_peso = 0
total_respostas = len(respostas)

for i, resposta in enumerate(respostas):
    total_peso += perguntas_selecionadas[i]["opcoes"][resposta][1]

if total_respostas > 0:
    media_peso = total_peso / total_respostas
else:
    media_peso = 0

media_peso = int(media_peso)
# Determinando o grau de sentimento
if media_peso == 1: 
    grau_sentimento = "Muita tristeza"
elif media_peso == 2: 
    grau_sentimento = "Tristeza moderada"
elif media_peso == 3: 
    grau_sentimento = "Neutro/Normal"
elif media_peso == 4: 
    grau_sentimento = "Felicidade moderada"
elif media_peso == 5: 
    grau_sentimento = "Muita felicidade"
else: 
    grau_sentimento = "Indeterminado"

print("\nPerguntas Selecionadas e Respostas:")
for i, pergunta in enumerate(perguntas_selecionadas): 
    print(f"{i+1}. {pergunta['pergunta']}")
    for j, opcao in enumerate(pergunta["opcoes"]): 
        marcado = "X" if respostas[i] == j else " " 
        print(f" [{marcado}] {opcao[0]}")

#print(f"\nMédia dos Pesos das Respostas: {media_peso}")
print(f"Grau de Sentimento: {grau_sentimento}")