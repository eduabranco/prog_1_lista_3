ordem=['Primeiro','Segundo','Terceiro','Quarto','Quinto']
pulos=[]
media=0
nome=input("Atleta: ")

for i in ordem:
    salto=float(input(f'{i} Salto: '))
    pulos.append(salto)
pulos.sort()
for i in range(len(pulos)):
    if i==0 or i==4:continue
    else:media+=pulos[i]
media/=3

print(f"""
Melhor salto: {pulos[4]}
Pior salto: {pulos[0]}
Media dos demais saltos: {media}

Resultado final:
{nome}: {media}
""")
