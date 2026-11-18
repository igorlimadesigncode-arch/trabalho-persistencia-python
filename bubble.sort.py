# bubble.sort.py
# Microatividade 2: ordenação de um array com o algoritmo Bubble Sort


def bubbleSort(array):
    """Ordena o array em ordem crescente usando Bubble Sort (in place)."""
    # Primeiro laço: cada passada "empurra" o maior valor restante para o fim
    for i in range(len(array)):
        # Segundo laço: compara os elementos adjacentes, de dois em dois
        for j in range(0, len(array) - i - 1):
            # Se o elemento j for maior que o j+1, troca os dois de lugar
            if array[j] > array[j + 1]:
                temp = array[j]          # variável auxiliar guarda array[j]
                array[j] = array[j + 1]  # array[j] recebe array[j+1]
                array[j + 1] = temp      # array[j+1] recebe o valor guardado


# Array de números com 15 posições, não ordenado
numeros = [64, 34, 25, 12, 22, 11, 90, 5, 78, 41, 3, 56, 19, 87, 30]

print("Array original:", numeros)

# Aplica o método bubbleSort ao array
bubbleSort(numeros)

# Imprime o array ordenado
print("Array ordenado:", numeros)