salario= float (input("Digite o seu salario:"))
pimposto = float (input ("Digite a porcentagem do imposto de renda :"))
psalario=salario*pimposto/100
print (f"O seu salario é {salario}")
print (f"A porcentagem do seu imposto de renda é {pimposto}")
salarioLiquido= salario-psalario
print (f"O seu salario liquido é de {salarioLiquido}")
