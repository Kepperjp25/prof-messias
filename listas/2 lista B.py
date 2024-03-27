a=[]
b=[]
for i in range(0,8):
 a.append(int(input("digite o {i+1} elemento de numero A: ")))
 b.append(a[i]+3)
print(f"O vetor B é: {b}")