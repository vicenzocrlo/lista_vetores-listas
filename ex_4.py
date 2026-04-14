lista = []

while True:
    if len(lista) == 0:
        entrada = int(input("Digite o número inteiro que deseja adicionar a lista: "))
        lista.append(entrada)

    elif len(lista) >= 1:
        entrada_2 = input("Você deseja adicionar mais um número a sua lista?: (S ou N): ") .upper()
        if entrada_2 == "S":
            entrada_3 = int(input("Digite o número inteiro que deseja adicionar a lista: "))
            lista.append(entrada_3)
        else:
            break

total = sum(lista)
print(total)