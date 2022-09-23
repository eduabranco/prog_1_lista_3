salarios=[]
abonos=[]
total=min=0

while True:
    salario=float(input("Salário: "))
    if salario==0:break
    elif salario<0:continue
    elif (salario*0.2)<=100:
        salarios.append(salario)
        abonos.append(100)
        total+=100
        min+=1
    else:
        salarios.append(salario)
        abonos.append(salario*0.2)
        total+=salario*0.2

print("Salário - Abono")

for i in range(len(salarios)):
    print(f"R${salarios[i]:.2f} - R${abonos[i]:.2f}")

abonos.sort()

print(f"""
Foram processados {len(salarios)} colaboradores
Total gasto com abonos: {total}
Valor mínimo pago a {min} colaboradores
Maior valor de abono pago: {abonos[len(abonos)-1]}
""")