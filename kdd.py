# kdd.py
# Trabalho Prático: glossário de palavras ordenadas (versão final)

ARQUIVO_ENTRADA = "loremipsum.txt"
ARQUIVO_SAIDA = "palavras_ordenadas.txt"

# Lista que armazenará as palavras (usando a classe list())
palavras = list()

# Leitura do arquivo com "with", percorrendo linha a linha
with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        # split separa a linha em palavras
        for palavra in linha.split():
            palavras.append(palavra)

# Ordenação com o método nativo do Python
palavras.sort()

# Impressão do resultado
print(f"Total de palavras: {len(palavras)}")
print(palavras)

# Criação do novo arquivo txt com as palavras ordenadas (uma por linha)
with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as saida:
    for palavra in palavras:
        saida.write(palavra + "\n")

print(f"Arquivo '{ARQUIVO_SAIDA}' criado com sucesso!")