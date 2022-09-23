print("""Selecione uma situação:
1- necessita da esfera
2- necessita de limpeza
3- necessita troca do cabo ou conector
4- quebrado ou inutilizado
""")
qnt1=qnt2=qnt3=qnt4=0
all=[]
while True:
    sit=input(f"Insira um número para a situação do mouse {len(all)+1}: ")
    if sit=='0':break
    elif sit=='1':all.append(sit)
    elif sit=='2':all.append(sit)
    elif sit=='3':all.append(sit)
    elif sit=='4':all.append(sit)
total=len(all)

print(f'Quantidade de mouses:{total}\n')
print(f"""Situação                               - Quantidade -   Percentual
1- necessita da esfera                 - {all.count('1')}          -   {(all.count('2')/(len(all)) *100):.2f}%
2- necessita de limpeza                - {all.count('2')}          -   {(all.count('1')/(len(all)) *100):.2f}%
3- necessita troca do cabo ou conector - {all.count('3')}          -   {(all.count('3')/(len(all)) *100):.2f}%
4- quebrado ou inutilizado             - {all.count('4')}          -   {(all.count('4')/(len(all)) *100):.2f}%
""")