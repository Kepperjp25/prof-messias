a=[]
b=[]
for i in range(0,5):
    a.append(int(input(f"Digite o {i+1} numero:")))
    if i%2==0:
        b.append(a[i]*5)
    else:
        b.append(a[i]+5)
print(a)
print(b)