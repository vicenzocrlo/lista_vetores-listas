
print("========CARRINHO=======")
carrrinho = []

entrada = input("O que você deseja adicionar ao seu carrinho de compras?: ")
carrrinho.append(entrada)
while True:

    if len(carrrinho)!= 0:
        confirmacao = input("Deseja adicionar mais algum produto ao seu carrinho?(S/N): ") .upper()
        if confirmacao == "S":
            entrada_2 = input("O que você deseja adicionar ao carrinho de compras?: ")
            carrrinho.append(entrada_2)
        elif confirmacao == "N":
            print("Fechando carrinho...")
            print(f"====CARRINHO====\n{carrrinho}")
            break
    else:
        entrada_3 = input("Você deve adicionar algum item ao seu carrinho antes de fechá-lo: ")
        carrrinho.append(entrada_3)


