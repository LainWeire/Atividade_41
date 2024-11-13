# Faça um programa que crie uma matriz M (com valores
# informados do usuário) e mostre a matriz com o dobro
# dos valores lidos (2*M).

l = int(input("Número de linhas: "))
c = int(input("Número de colunas: "))

m = []
for i in range(l):
    linha = []
    for j in range(c):
        v = float(input(f"Valor para a posição ({i+1}, {j+1}): "))
        linha.append(v)
    m.append(linha)

for i in range(l):
    for j in range(c):
        m[i][j] *= 2

print("Matriz:")
for linha in m:
    print(linha)
    