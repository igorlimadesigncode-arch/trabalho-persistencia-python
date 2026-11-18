# array.sort.py
# Microatividade 1: ordenação de arrays em Python com o método sort()

import random

# ---------------------------------------------------------
# PARTE 1: array de 15 inteiros aleatórios, não ordenados
# ---------------------------------------------------------
numeros = [random.randint(1, 100) for _ in range(15)]

print("=== ARRAY DE INTEIROS ===")
print("Original (não ordenado):   ", numeros)

# Ordenação crescente (comportamento padrão do sort)
numeros.sort()
print("Ordenado (crescente):      ", numeros)

# Ordenação decrescente, com os parâmetros key=None e reverse=True
numeros.sort(key=None, reverse=True)
print("Ordenado (decrescente):    ", numeros)

# ---------------------------------------------------------
# PARTE 2: arrays de strings (nome, dataNascimento, cpf, rg)
# ---------------------------------------------------------
nomes = ["Carlos Silva", "Ana Souza", "Beatriz Lima", "Daniel Costa", "Fernanda Alves"]
datas_nascimento = ["15/03/1995", "02/11/1988", "27/07/2001", "09/01/1992", "30/12/1999"]
cpfs = ["529.982.247-25", "111.444.777-35", "390.533.447-05", "168.995.350-09", "745.123.980-61"]
rgs = ["12.345.678-9", "98.765.432-1", "45.678.912-3", "23.456.789-0", "34.567.891-2"]

# Dicionário para percorrer todos os arrays com o mesmo código
dados = {
    "nome": nomes,
    "dataNascimento": datas_nascimento,
    "cpf": cpfs,
    "rg": rgs,
}

for campo, lista in dados.items():
    print(f"\n=== ARRAY DE STRINGS: {campo} ===")
    print("Original (não ordenado):   ", lista)

    lista.sort()
    print("Ordenado (crescente):      ", lista)

    lista.sort(key=None, reverse=True)
    print("Ordenado (decrescente):    ", lista)