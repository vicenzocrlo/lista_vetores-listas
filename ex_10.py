lista = []

print("Vamos realizar a soma dos seus números?")
entrada = float(input("Digite o número que deseja adicionar a sua lista ou 0 para finalizar: "))

while entrada != 0:
    lista.append(entrada)
    entrada = float(input("Digite o número que deseja adicionar a sua lista ou 0 para finalizar: "))


soma = sum(lista)


print(f"Sua lista após a adição de todos os números: {lista}\n")
print(f"A soma de todos os números da sua lista: {soma}")


