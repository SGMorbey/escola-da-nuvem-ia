def calcular_idade_em_dias(total_dias):
    anos = total_dias // 365
    dias_restantes = total_dias % 365
    meses = dias_restantes // 30
    dias = dias_restantes % 30
    
    print(f"{anos} ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)")

if __name__ == "__main__":
    # Exemplo de entrada
    total_dias = int(input("Digite a idade em dias: "))
    calcular_idade_em_dias(total_dias)