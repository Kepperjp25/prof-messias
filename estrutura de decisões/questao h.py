base=int(input("Digite um numero:"))
expoente=int(input("Digite o expoente:"))
potencia=1
for i in range(expoente):
    potencia=potencia*base
    print("potencia de {} elevado a {} é igual a {}". format(base,expoente,potencia))