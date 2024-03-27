a=int(input("Digite o lado a:"))
b=int(input("Digite o lado b:"))
c=int(input("Digite o lado c:"))
#testando se os lados forma um triangulo
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print("Triangulo equulatero.")
    elif a==b or a==c or b==c:
        print("Triangulo isosceles.")
    else:
        print("Triangulo escaleno.")
else:
    print("Os lados nao formam um triangulo.")