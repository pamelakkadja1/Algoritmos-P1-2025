#Modulo = %
#Exemplo 4%2=0; modulo é o que sobra (resto)
modulo= 5 % 4
print(modulo)

ano=int(input("Digite o ano :"))

ebissexto="N"

if(ano % 4 == 0):
    ebissexto="S"
    if(ano % 100==0 and ano %400!=0):
        ebissexto="N"
if(ebissexto=="S"):
    print("O ano é bissexto!")
else:
    print("O ano não é bisexto!")

        