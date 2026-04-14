lista_nomes = ["Vicenzo", "Henrique","Joaquim", "Carlo", "Letícia", "Giovana"]

while True:
    seu_nome = input("Digite o nome que você deseja verificar se está na lista: ")

    if seu_nome in lista_nomes:
        print(f"O nome {seu_nome} está presente na lista.")
        break
    else:
        print(f"O nome {seu_nome} não está presente na lista")
        