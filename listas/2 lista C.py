a=[]
b=[]
c=[]
for i in range(5):
    a.append(int(input(f"Digite o {i+1} numero de A:")))
    b.append(int(input(f"Digite o {i+1} numero de B:")))
    c.append(a[i]-b[i])
print(c)