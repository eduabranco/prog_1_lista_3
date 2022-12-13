lista=[]
total=0
def bytecalc(raw):
    global lista
    Mb=raw/(2**20)
    return Mb

def percalc(total,raw):
    perc=(raw*100)/total
    return perc

with open('usuarios.txt') as f: lista = f.readlines()

for i in range(len(lista)):
    lista[i]=lista[i].split()
    lista[i][1]=int(lista[i][1])

for i in range(len(lista)):total+=lista[i][1]
total=bytecalc(total)
for i in range(len(lista)):
    lista[i][1]=bytecalc(lista[i][1])
    lista[i].append(percalc(total,lista[i][1]))
print(lista)



print(f"""
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr. Usuário        Espaço utilizado        % do uso
""")
for i in range(len(lista)):
    print(f'{i+1}   {lista[i][0]}         {lista[i][1]:.2f}MB         {lista[i][2]:.2f}%')
print(f'Espaço total ocupado:{total:.2f}MB')
print(f'Espaço médio ocupado:{(total/len(lista)):.2f}MB')
