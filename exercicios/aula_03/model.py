from sklearn.linear_model import LinearRegression
import numpy as np

# Dados de treino
horas_estudo = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Valores de referência
notas = np.array([40, 50, 60, 70, 80])

# Treinar o modelo
modelo = LinearRegression()
modelo.fit(horas_estudo, notas)

# Perguntar ao usuário
horas = float(input("Digite o número de horas estudadas: "))

# Fazer a previsão
nota_prevista = modelo.predict([[horas]])

# Exibir o resultado
print(f"Com {horas} horas de estudo, a nota prevista é {nota_prevista[0]:.2f}")
