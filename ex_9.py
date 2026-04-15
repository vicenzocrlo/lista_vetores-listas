notas = [5, 6, 7, 3, 8]

media_final = sum(notas)/ len(notas)
print(f"A média da turma foi {media_final}\n")

for nota in notas:
    if nota >= media_final:
        print(f"A nota {nota} está acima da média {media_final}\n")
    else:
        print(f"A nota {nota} está abaixo da média {media_final}\n")

