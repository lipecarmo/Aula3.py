# contador = 1

# while contador < 5:
#     print(contador)
#     contador += 1



# senha = '12345'

# while True:

#     senha_digitada = input('Digite sua senha:')

#     if senha_digitada == senha:

#         print('Autenticado com sucesso.')
#         break

#     else:

#         print('Senha incorreta')


# Atividade 01:
# Contagem de 1 a 10:
# Crie um programa que use um laço while
# para contar de 1 a 10 e exibir cada número.

# contador = 1

# while contador < 11:
#     print(contador)
#     contador +=1


# Atividade 02:
# Soma de Números de 1 a 100:
# Escreva um programa que use um laço while para
# somar os números de 1 a 100 e exiba o resultado.

# soma = 0
# numero = 1

# while numero < 101:
#     soma += numero
#     numero +=1

# print(f'A soma dos números de 1 até 100 é:{soma}')

# Atividade 03:
# Tabuada de um Número:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10).

# numero = int(input('Digite um numero:'))
# multiplicador = 1 
# while multiplicador < 11:
#     print (f'{numero}*{multiplicador} = {numero*multiplicador}')
#     multiplicador +=1

# Atividade 04:
# Contagem Regressiva:
# Desenvolva um programa que use um laço while para exibir
# uma contagem regressiva de 10 até 1 e, em seguida, exiba
# "Feliz Ano Novo!".

# contagem = 10

# while contagem > 0:
#     print (contagem)
#     contagem -=1

# print('Feliz Ano Novo!')

# while True:
#     print('Menu:')
#     print('1 - OPCAO 1')
#     print('2- OPCAO 2')
#     print('3- OPCAO 3')
#     print('4- OPCAO 4')
#     opcao = input('->')
#     if opcao == '1':
#         print('Voce escolheu a opcao 1')
#     elif opcao == '2':
#         print('Voce escolheu a opcao 2')
#     elif opcao == '3':
#          print('Voce escolheu a opcao 3')
#     elif opcao == '4':
#          print('Voce escolheu a opcao 4')
#          break

# Atividade 05:
# Contagem até o Número Inserido:
# Crie um programa que solicite um número ao usuário e use
# um laço while para contar de 1 até o número inserido,
# exibindo apenas os números ímpares.

# numero = int(input('Digite um numero:'))
# contador = 1
# while contador <= numero:
#     if contador % 2 != 0:
#         print(contador)

#     contador +=1
 
# Atividade 06:
# Soma de Números Positivos:
# Escreva um programa que solicite números ao usuário até
# que ele digite um número negativo, somando apenas os
# números positivos inseridos.

# positivos = 0
# while True:
#     numero = int(input('Digite um número:'))
#     if numero > 0:
#         positivos += numero
#     elif numero <0:
#         break

#     print(f'O resultado da soma dos positivos é:{positivos}')

# Atividade 07:
# Tabuada com Condicional:
# Faça um programa que solicite um número ao usuário e use
# um laço while para exibir a tabuada desse número (de 1 a 10),
# mas apenas para os resultados que forem múltiplos de 3.

# numero = int (input('Digite um numero:'))
# multiplicador = 1
# while multiplicador < 11:
#     if (numero * multiplicador) % 3 == 0:
#         print (f'{numero} X {multiplicador} = {numero*multiplicador}')

#     multiplicador +=1

# Atividade 08:
# Média de Notas:
# Desenvolva um programa que solicite as notas dos alunos até
# que o usuário digite -1. Calcule e exiba a média das notas
# inseridas.

# soma_notas = 0
# qtd_notas = 0
# while True:
#     nota = float(input('Digite a nota:'))
#     if nota == -1:
#        break
#     else:
#         soma_notas += nota
#         qtd_notas += 1
# print(f'A media das notas digitadas é:{soma_notas/qtd_notas}')

# soma = 0 
# while soma <= 50:
#     numero= int(input('Digite o numero:'))
#     soma += numero

# print(soma)

