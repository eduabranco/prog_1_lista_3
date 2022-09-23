cardapio={'100' : 1.2 , '101' : 1.3 , '102' : 1.50 , '103' : 1.2 , '104' : 1.3 , '105' : 1.0 }
cq=bs=bo=hb=cb=rf=0
while True:
    escolha=input("Código (Para terminar o pedido, não escreva nada)\n")
    if escolha=="":break
    elif escolha=='100':
        qnt=int(input("Quantidade de Cachorro Quente?\n"))
        cq+=cardapio['100']*qnt
    elif escolha=='101':
        qnt=int(input("Quantidade de Bauru Simples?\n"))
        bs+=cardapio['101']*qnt
    elif escolha=='102':
        qnt=int(input("Quantidade de Bauru com ovo?\n"))
        bo+=cardapio['102']*qnt
    elif escolha=='103':
        qnt=int(input("Quantidade de Hambúrguer?\n"))
        hb+=cardapio['103']*qnt
    elif escolha=='104':
        qnt=int(input("Quantidade de Cheeseburguer?\n"))
        cb+=cardapio['104']*qnt
    elif escolha=='105':
        qnt=int(input("Quantidade de Refrigerante?\n"))
        rf+=cardapio['105']*qnt
total=cq+bs+bo+hb+cb+rf
print(f""""
Cachorro Quente ==> R${cq:.2f}
Bauru Simples ==> R${bs:.2f}
Bauru com ovo ==> R${bo:.2f}
Hambúrguer ==> R${hb:.2f}
Cheeseburguer ==> R${cb:.2f}
Refrigerante ==> R${rf:.2f}

Total: R${total:.2f}
""")
input()
