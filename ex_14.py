print("Vamos descobrir quantas strings da nossa lista começam com A?")
strings = ["Amor", "Anjos", "Bola", "Python", "Lists"]

contagem = sum(1 for n in strings if n.startswith("A"))

print(f"Quantidade de strings que começam com a letra A: {contagem} ")
