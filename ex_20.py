
menu = '''
======== LISTA DE TAREFAS ========
Olá, seja bem vindo!
Escolha uma opção abaixo para darmos inicio a nossa organização de tarefas!

[1] Adicionar
[2] Remover
[3] Exibir
[4] Sair

'''
lista_tarefas = []
print(menu)

while True:
    entrada = int(input("\nDigite o número da operação que você deseja realizar: "))

    if entrada == 1:
        adicionar = input("\nDigite a tarefa que você deseja adicionar a sua lista: ")
        if adicionar not in lista_tarefas:
            lista_tarefas.append(adicionar)
            print("A tarefa foi adicionada a sua lista! ")
        else:
            adicionar_mesma_tarefa= input("Esta tarefa já está na sua lista! Deseja realmente adiciona-lá novamente?(S/N): ") .upper()
            if adicionar_mesma_tarefa == "S":
                lista_tarefas.append(adicionar)
                print("A Tarefa foi adicionada a sua lista! ")

    elif entrada == 2:
        remover = input("\nDigite a tarefa que você deseja remover da sua lista: ")

        if remover in lista_tarefas:
            lista_tarefas.remove(remover)
            print("A Tarefa foi removida da sua lista. ")
        else:
            print("Esta tarefa não existe na lista! Tente novamente")

    elif entrada == 3:
        if len(lista_tarefas) == 0:
            print(f"========== TAREFAS ==========\n")
            print("Nenhuma tarefa adicionada!")
  
        else:
            print(f"========== TAREFAS ==========\n")
            for tarefa in lista_tarefas:
                print(f'\t{tarefa}')

    elif entrada == 4:
        print("Saindo...")
        break

    else:
        print("\nOpção inválida, digite a sua opção de escolha novamente!")




