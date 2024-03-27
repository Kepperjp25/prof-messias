primeiro=1
segundo=1
print(primeiro)
print(segundo)
cont=2
while cont<100:
    proximo=primeiro+segundo
    print(proximo)
    primeiro=segundo
    segundo=proximo
    cont+=1
print("Fim da serie de Fibonacci")