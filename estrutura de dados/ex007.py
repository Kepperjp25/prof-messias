#Exercicio 7
a=input("Nome da pessoa:")
b=input("Sexo da pessoa F ou M:")
if b.upper() == "M":
    print("Ilmo. Sr", a)
elif b.upper() == "F":
    print("Ilma. Sra", a)