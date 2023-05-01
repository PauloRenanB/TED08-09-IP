# 2. Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
# números repetidos no vetor VET e em que posições se encontram.

num  = []

for i in range(10):
    numero = int(input(f'Digite o {i+1}º número: '))
    num.append(numero)

repetidos = []
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] == num[j]:
            if num[i] not in repetidos:
                repetidos.append(num[i])
            print(f'O número {num[i]} está nas posições {i+1} e {j+1}')

if len(repetidos) > 0:
    print('Os seguintes números estão repetidos: ')
    print(repetidos)
else:
    print('Não foram encontrados números repetidos.')