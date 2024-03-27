a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
d=b**2-4*a*c
r1=(-b+(d**(1/2)))/(2*a)
r2=(-b-(d**(1/2)))/(2*a)
if d==0:
    print(f"existem duas raizes reais iguais, {r1}, {r2}")
if d>0:
    print(f"existem duas raizes reais distintas, {r1}, {r2}")
else:
    print("nao existem raizes reais")
 

