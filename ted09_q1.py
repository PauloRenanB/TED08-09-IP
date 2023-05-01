# 1. Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20
# números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.

vetor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
vetor_inv = []

# vetor_inv = list(range(20, -1, -1))
# ou
vetor_inv = vetor[::-1]

print(vetor_inv)