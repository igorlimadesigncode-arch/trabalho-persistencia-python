`markdown
# Trabalho Prático: Persistência de Dados em Python

Este projeto reúne exercícios de **ordenação** e de **leitura e escrita de arquivos de texto** em Python, culminando em um script (`kdd.py`) que lê um texto, ordena as palavras e grava o resultado em um novo arquivo.

## Arquivos do projeto

| Arquivo | Finalidade |
|---|---|
| `array.sort.py` | Ordenação com o método nativo `sort()` |
| `bubble.sort.py` | Algoritmo Bubble Sort |
| `selection.sort.py` | Algoritmo Selection Sort |
| `ler.txt.py` | Leitura do arquivo `loremipsum.txt` |
| `escrever.txt.py` | Escrita de conteúdo em `texto.txt` |
| `kdd.py` | Leitura, ordenação e gravação das palavras |
| `loremipsum.txt` | Texto de entrada |
| `texto.txt` | Arquivo gerado pelo script de escrita |
| `palavras_ordenadas.txt` | Saída do `kdd.py` com as palavras em ordem |

## Funcionalidades

### Ordenação

- Ordenação com o método nativo `sort()`.
- Implementação manual do **Bubble Sort**.
- Implementação manual do **Selection Sort**.

### Persistência em arquivos

- Leitura de arquivo de texto com `open()`.
- Escrita de arquivo de texto.
- Uso de codificação UTF-8 para preservar acentos.

### Script `kdd.py`

- Lê o texto de `loremipsum.txt` e separa as palavras.
- Ordena as palavras com `sort()`.
- Grava o resultado em `palavras_ordenadas.txt`.
- Compara o tempo de execução de cada método de ordenação.

## Desempenho

Medição com **69 palavras**:

| Método | Tempo (s) |
|---|---|
| Bubble Sort | 0,000081 |
| Selection Sort | 0,000064 |
| `sort()` nativo | 0,000007 |

O `sort()` nativo foi o mais rápido, o que é esperado: ele usa o algoritmo Timsort, implementado em C, enquanto Bubble e Selection Sort têm complexidade \(O(n^2)\).

## Como executar

1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Execute o script desejado:
bash python kdd.py

No Windows, também é possível usar `py .\kdd.py`. Os demais scripts rodam do mesmo modo, trocando o nome do arquivo.

## Tecnologias

- Python 3
- Manipulação de arquivos de texto
- Algoritmos de ordenação

## Ambiente

- VS Code e Windows
- Python 3

## Autor

Igor Lima
