
#Print é uma saida do codigo phyton 
print('Olá mundo')

#variavel de texto 

# Nome é uma variavel de texto (str)
# Idade é uma variavrl de número inteiro (int)
# Altura é uma variavrl de decimal (float)

nome = 'Vitória'
idade = 16
altura = 1.65

print (nome)
print (idade)
print (altura)

soma = 27+15
print (soma)

subtracao = 27-15
print (subtracao)

multiplicacao = 27*15 
print (multiplicacao)

divisao = 27/15
print (divisao)

um = 18
dois = 9

somaVar = um/dois 

print (f'Nome:{nome}')
print (f'Idade:{idade}')
print (f'Altura:{altura}')

# input = entrada de dados
#
cpfConvertido = int(input("Digite o seu CPF:  "))

cpfConvertido = float(input("Digite o seu CPF:  "))

cpfConvertido = str(input("Digite o seu CPF:  "))
# > maior que
# < menor que 
# >= maior ou igual a 
# <= menor ou igual a 
# == igual a 
# != diferente de 

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
elif idade >= 16:
    print("Pode votar")
elif idade>= 0 and idade<16 :
    print ("Menor de idade")
else :
    print ("Idade invalida")

Nome = str(input("Digite seu nome: "))

