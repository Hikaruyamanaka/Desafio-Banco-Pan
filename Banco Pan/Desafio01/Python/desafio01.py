# Find the Longest Word
# This coding challenge is all about working with words in a sentence. It's a good exercise to get better at handling text.

# The Problem: Your task is to write a function that looks at a sentence and figures out which word is the longest. Then, it tells you how many letters that word has.
# Example Input:
# "The quick brown fox jumped over the lazy dog"

# Example Output:
# 6 (because "jumped" is the longest word)
# Seu input para o desafio será: “Banco Pan, um banco completo com soluções inteligentes”



print('\n-+-+-+-+-+-+-   DESAFIO 01   -+-+-+-+-+-+-\n')


# Opção 1
def encontre_maior_palavra(sentence):

    # Divide a sentença em palavras
    palavras = sentence.split()  

    # Inicializa uma string vazia para armazenar a palavra mais longa
    maior_palavra = ""  

    # Inicializa a variável para armazenar o comprimento da palavra mais longa
    max_tamanho = 0  

    # Percorre cada palavra na lista 'words'
    for palavra in palavras:

        # Se o comprimento da palavra atual for maior que 'max_length'
        if len(palavra) > max_tamanho:  

            # Atualiza o comprimento da palavra mais longa
            max_tamanho = len(palavra)  

            # Atualiza a palavra mais longa
            maior_palavra = palavra     
    
    # Retorna a palavra mais longa
    return maior_palavra  

# Testando com o input fornecido
sentence = "Banco Pan, um banco completo com soluções inteligentes"

# Saída Esperada: "inteligentes"
print(f'Saída: {encontre_maior_palavra(sentence)}')  



# Opção 2
def encontre_maior_palavra(sentence):

    # Divide a sentença em palavras
    palavra = sentence.split()  

    # Encontra a palavra mais longa
    maior_palavra = max(palavra, key=len)

    # Retorna a palavra mais longa  
    return maior_palavra 
 
# Testando com o input fornecido
sentence = "Banco Pan, um banco completo com soluções inteligentes"

# Saída Esperada: "inteligentes"
print(f'Saída: {encontre_maior_palavra(sentence)}')  
  