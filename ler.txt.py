# ler.txt.py
# Microatividade 4: leitura de dados a partir de um arquivo externo

# a) Atribui à variável o conteúdo do arquivo, usando o método open
arquivo = open("loremipsum.txt", "r", encoding="utf-8")

# b) Imprime todo o conteúdo do arquivo
print("=== CONTEÚDO COMPLETO ===")
print(arquivo.read())

# c) Imprime apenas a primeira linha
arquivo.seek(0)
print("\n=== PRIMEIRA LINHA ===")
print(arquivo.readline())

# d) Imprime apenas os 3 primeiros caracteres
arquivo.seek(0)
print("=== 3 PRIMEIROS CARACTERES ===")
print(arquivo.read(3))

# Fecha o arquivo aberto com open
arquivo.close()

# e) Usa a instrução with: abre, armazena o conteúdo em uma variável e imprime
with open("loremipsum.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

print("\n=== CONTEÚDO LIDO COM 'WITH' ===")
print(conteudo)