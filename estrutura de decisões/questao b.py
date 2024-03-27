while True:
    a = int(input("Digite o numero para a tabuada do 2:"))
    print("Tabuada do 2:", a)
    i = 1
    for i in range(1,11):
        print(i, "x", a, "=", i*a)
    continua=input("Deseja continuar? (sim/nao):")
    if continua=="nao":
        break