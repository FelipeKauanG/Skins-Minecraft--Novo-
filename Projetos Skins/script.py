nomes = r"Nomes Alunos.txt"
lista = []
with open(nomes, mode="r", encoding="UTF-8") as arquivo:
    lista = sorted(arquivo.readlines())



for num, nome in enumerate(lista):
    print(f"\033[34m{num+1} - {nome.title()}\033[m", end="")

with open(nomes, mode="w", encoding="UTF-8") as arquivo:
    arquivo.writelines(lista)