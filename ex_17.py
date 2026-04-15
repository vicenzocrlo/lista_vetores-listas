numeros = [2, 4, 6, 10, 25]
fatorial = []

for n in numeros:
    inicial = 1

    for i in range(1, n +1):
        inicial *= i
    fatorial.append(inicial)  

print(fatorial)  

