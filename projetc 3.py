'''Verificar se um numero é divisivel pro 3 (multiplos divisores de um numero)'''

numero = input("Digite um número: ")
soma = 0

for digito in numero: #laço realiza a separação e soma dos digitos do numero apresentado pelo usuário
    if digito.isdigit():
        soma += int(digito)
if int(numero) % 2 == 0:
    print('O numero que você digitou é multiplo de 2!')
else: 
    print('O numero que você digitou NÃO é multiplo de 2!')
if int(numero) % 5 == 0:
    print('O numero que você digitou é multiplo de 5!')
else:
      print('O numero que você digitou NÃO é multiplo de 5!')

while soma > 9:  #para verificar se é multiplo de 3 é realizada a soma dos algarismos caso a soma do primeiro numero digitada seja maior que 9.
    numero = str(soma)
    soma = 0
    for digito in numero:
        if digito.isdigit():
            soma += int(digito)
#print("A soma dos dígitos é:", soma)
#print("O resultado final é:", soma)

if soma == 3:
            print('O numero que você digitou é multiplo de 3!')
elif soma == 6: 
            print('O numero que você digitou é multiplo de 3!')
elif soma == 9:
            print('O numero que você digitou é multiplo de 3!')     
else:
    print('O numero que você digitou NÃO é multiplo de 3')
   

input('Aperte qualquer tecla para encerrar')


