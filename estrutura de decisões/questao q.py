areatotal=0
resp='sim'
while resp!='nao':
    comodo=input("Digite o comodo:")
    largura=float(input("Digite a largura do comodo:"))
    comprimento=float(input("Digite o comprimento do comodo:"))
    areacomodo=largura*comprimento
    print("A area do comodo", comodo, "é", areacomodo)
    areatotal+=areacomodo
    resp=input("Deseja continuar?:")
    if resp=='nao':
        break
print("A area total da casa é:", areatotal)