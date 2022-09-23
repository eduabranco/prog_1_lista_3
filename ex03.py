st=nd=rd=th=nul=branco=0
print("1- Jose\n2- João\n3- Jonas\n4- JoJo\n5- Voto nulo\n6- Voto em branco")
while True:
    x=input("""\nVote: """)
    if x=='1':st+=1
    elif x=='2':nd+=1
    elif x=='3':rd+=1
    elif x=='4':th+=1
    elif x=='5':nul+=1
    elif x=='6':branco+=1
    elif x=='0':break
    else:nul+=1
total=st+nd+rd+th+nul+branco
print(f'''\n
Votos para Jose : {st}\n
Votos para João : {nd}\n
Votos para Jonas : {rd}\n
Votos para JoJo : {th}\n
Votos nulos : {nul}\n
Votos em branco : {branco}\n
Percentagem - Votos nulos sobre o total: {(nul/total)*100}%\n
Percentagem - Votos em branco sobre o total: {(branco/total)*100}%
''')
input()