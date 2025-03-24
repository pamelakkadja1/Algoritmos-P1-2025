num1=float(input("Digite o primeiro numero:"))
num2=float(input("Digite o segundo numero:"))
if(num1==num2):
    print(f"{num1} é igual a {num2}")
else:
 if(num1<num2):
    print(f"O primeiro numero é menor que o segundo, {num1}<{num2}")
 else:
    print(f"O segundo numero é menor que o primeiro, {num1}>{num2}")