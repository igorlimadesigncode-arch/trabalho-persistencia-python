# escrever.txt.py
# Microatividade 5: escrita de dados em um arquivo externo

# a) Abre um arquivo ainda não existente ("w" cria o arquivo) e o atribui a uma variável
arquivo = open("texto.txt", "w", encoding="utf-8")

# b) Cria uma lista usando a sintaxe list()
texto = list()

# c) Usa o método append para adicionar algumas frases à lista
texto.append("Python é uma linguagem de programação versátil.\n")
texto.append("Este arquivo foi criado pelo script escrever.txt.py.\n")
texto.append("A escrita em arquivos usa o modo 'w' do método open.\n")
texto.append("Cada frase da lista vira uma linha do arquivo.\n")

# d) Escreve no arquivo aberto o conteúdo da lista
arquivo.writelines(texto)

# Fecha o arquivo para garantir que os dados sejam gravados em disco
arquivo.close()

print("Arquivo 'texto.txt' criado com sucesso!")