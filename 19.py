num=int(input("Digite um numero maior que 0 e mnor que 1000:"))

centenas=0
dezenas=0
unidades=0
saidac=""
saidad=""
saidau=""
if(num>99):
    centenas=num//100
    num=num%100
if(num>9):
    dezenas=num//10
    num=num%10
if(centenas>1):
    saidac= saidac+"Centenas"
elif(centenas==1):
    saidac=saidac+"Centena"
if(dezenas>1):
    saidad=saidad+"Dezenas"
elif(dezenas==1):
    saidad=saidad+"Dezena"
if(unidades>1):
    saidau=saidau+"Unidades"
elif(unidades==1):
    saidau=saidau+"unidade"

print(f"Os seguintes dados foram obtidos:\n {saidac}:{centenas}.\n {saidad}:{dezenas}.\n{saidau}:{unidades}.")

    