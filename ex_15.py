
numeros = []
for numero in range(10):
    entrada = float(input(f"Digite o seu {numero +1}º número: "))
    numeros.append(entrada)

numeros.sort()
print(numeros)