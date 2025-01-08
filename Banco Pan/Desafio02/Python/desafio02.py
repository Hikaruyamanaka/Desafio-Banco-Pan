# Array Rotation
# This challenge is about moving numbers around in a list. It's useful for rearranging data.

# The Problem: You have a list of numbers. You need to move the numbers to the right by a certain amount. The user will tell you how many times.
# Example:
# Input list: [1, 2, 3, 4, 5] 
# Shifts: 2

# Output list: [4, 5, 1, 2, 3]

# Seu input para o desafio será: 
# Array: 1, 2, 3, 4, 5, 6, 7
# Shifts: 4


print('\n-+-+-+-+-+-+-   DESAFIO 02   -+-+-+-+-+-+-\n')

# Lista do desafio
lista = [1, 2, 3, 4, 5, 6, 7]

# Quantidade de vezes para rotacionar
rotacoes = 4

# Criando uma nova lista para o resultado
lista_rotacionada = [0] * len(lista)

for i in range(len(lista)):

    # Calcule a nova posição
    nova_posicao = (i + rotacoes) % len(lista)

    # Coloque o elemento na nova posição
    lista_rotacionada[nova_posicao] = lista[i]

# Imprima o resultado
print(f'Saída: {lista_rotacionada}')  

