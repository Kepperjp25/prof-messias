a= int(input("Digite um numero:"))
b= int(input("Digite um numero:"))
c= int(input("Digite um numero:"))
if a>b:
    a,b=b,a
if b>c:
    b,c=c,b
if a>b:
    a,b=b,a
print(a,b,c)