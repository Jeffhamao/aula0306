   #Descobrindo o tamanho da lista
nomes = ["Wilson", "Bianca", "Ronaldo", "Silmara", "Juliano"]

print(len(nomes))
    #Saber se existe um elemento na lista
if "Wilson" in nomes:
    print("Está na lista")
else:
    print("Não está na Lista")
    
    #A posição de um elemento na lista
indice = nomes.index("Bianca")
print(f"A Bianca está no indice {indice}")

    #Percorrer a lista
for nome in nomes:
    print(nome)

    #Percorrer a lista com indice e valor
for name, nome in enumerate(nomes):
    print(name, nome)

    #Limpar toda a lista
nomes.clear()
print(nomes)