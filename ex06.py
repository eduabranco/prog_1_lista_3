notas=[]
media=0
nome=input("Atleta: ")

for i in range(7):
    nota=float(input(f'Nota: '))
    notas.append(nota)
notas.sort()
for i in range(len(notas)):
    if i==0 or i==6:continue
    else:media+=notas[i]
media/=5

print(f"""
Resultado final:
Atleta: {nome}
Melhor nota: {notas[6]}
Pior nota: {notas[0]}
Media : {media:.2f}
""")