gabarito=['A','B','C','D','E','E','D','C','B','A']
for i in enumerate(gabarito):
    print(i)
notas=[]
media=0
while True:
    nota=0
    yorn=input("Prova para corrigir? (s/n)\n")
    if yorn=='s':
        for i in range(len(gabarito)):
            q=input(f"Resposta para questão {i+1}: ")
            if q.upper()==gabarito[i]:nota+=1
        media+=nota
        notas.append(nota)
        print(f'nota : {nota}')
    elif yorn=='n': break
notas.sort()
media/=len(notas)
print(f"""
Maior nota : {notas[len(notas)-1]}
Menor nota : {notas[0]}
Total de alunos participantes: {len(notas)}
Média: {media}
""")
input()