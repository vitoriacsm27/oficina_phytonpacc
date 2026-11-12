nome = str(input("Digite seu nome: "))

nota1 = float(input("Digite sua primeira nota aqui: "))
nota2 = float(input("Digite sua segunda nota aqui: "))
nota3 = float(input("Digite sua terceira nota aqui: "))

media = (nota1+nota2+nota3)/3

if media <5 :
    print ("Reprovado")
elif media >=5 and media <=7 :
    print ("Recuperação")
elif media >=7 : 
    print ("Aprovado")