list_par = []
list_impar = []

for numero in range(10):
    entrada = int(input(f"Digite o seu {numero +1}º número: "))
    if entrada % 2 == 0:
        list_par.append(entrada)
    elif entrada % 3 == 0:
        list_impar.append(entrada)
    else:
        pass

print(list_par)
print(list_impar)