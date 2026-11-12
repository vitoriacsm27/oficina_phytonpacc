"""Crie um programa que solicite a idade de uma pessoa e classifique
o valor do ingresso conforme as regras:
    Menor que 12 anos o ingresso será de R$12.00
    12 a 17 anos o ingresso será de R$15.00
    Acima de 18 anos o ingresso será de R$25.00
"""

print ("Olá! Bem vindo ao PACCINEMA :)")

nome = str(input("Qual é o seu nome?: "))
idade = int(input("sua idade: "))

if idade >=18 :
    print ("Ingresso apartir de R$25.00")
elif idade >=12 and idade <=17 :
    print ("Ingresso apartir de R$15.00")
elif idade >=0 and idade <=12 :
    print ("Ingresso apartir de R$12.00")
