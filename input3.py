print ("Olá! Bem vindo ao PAC :)")

nome = str(input("Qual é o seu nome?: "))
idade = int(input("sua idade: "))
if idade >=18 :
    print ("Adulto")
elif idade >=14 and idade <=17 :
    print ("Adolecente")
elif idade >=0 and idade <=13 :
    print ("Criança")

print (f'O usuario {nome} tem {idade} anos!')