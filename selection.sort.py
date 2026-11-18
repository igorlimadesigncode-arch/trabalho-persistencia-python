# selection.sort.py
# Microatividade 3: ordenação de um array com o algoritmo Selection Sort

# Array com 15 números inteiros, sem nenhuma ordenação
array = [64, 34, 25, 12, 22, 11, 90, 5, 78, 41, 3, 56, 19, 87, 30]

print("Array original:", array)

# Primeiro laço: percorre todas as posições do array
for i in range(len(array)):
    # Variável que guarda a posição do menor elemento encontrado até agora
    menor = i

    # Segundo laço: procura o menor elemento entre i+1 e o fim do array
    for j in range(i + 1, len(array)):
        # Se o elemento na posição "menor" for maior que o da posição j,
        # então j passa a ser a posição do menor elemento
        if array[menor] > array[j]:
            menor = j

    # Troca: coloca o menor elemento encontrado na posição i
    array[i], array[menor] = array[menor], array[i]

# Imprime o array ordenado
print("Array ordenado:", array)