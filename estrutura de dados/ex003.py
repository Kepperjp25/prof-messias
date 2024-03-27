#Começo do exercicio 1
n1=float(input("Primeira nota do aluno:"))
n2=float(input("Segunda nota do aluno:"))
n3=float(input("Terceira nota do aluno:"))
n4=float(input("Quarta nota do aluno:"))
soma=n1+n2+n3+n4
media=soma/4
if media>=7:
    print(f"Aluno aprovado, a media do aluno foi {media}.")
else:
    print(f"Aluno reprovado, a media do aluno foi {media}.")
    ex=float(input("Solicitar nota final:"))
    exs=(ex+media)/2
    if exs>=5:
        print(f"Aluno aprovado em exame final com a media:{exs}")
    else:
     print(f"Aluno reprovado com a media {exs}")