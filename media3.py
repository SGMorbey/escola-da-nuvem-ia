# Leia quatro notas com uma casa decimal
N1, N2, N3, N4 = map(float, input().split())

# Calcule a média ponderada
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Media: {media:.1f}")

# Verifique as condições de aprovação, reprovação ou exame
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    # Leia a nota do exame
    exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {exame:.1f}")

    # Recalcule a média final
    media_final = (media + exame) / 2

    # Verifique a condição após o exame
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
