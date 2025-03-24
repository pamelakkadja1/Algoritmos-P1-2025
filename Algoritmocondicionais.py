num1 = float (input ("Digite a primeira nota :"))
num2 = float (input("Digite a segunda nota :"))
num3 = float (input("Digite a terceira nota :"))
media = (num1+num2+num3)/3
if(media >= 7):
 print (f"APROVADO, sua media é {media}")
else:
 print (f"REPROVADO, sua media foi {media}")