carros=[]
v=[]
gas=2.25

for i in range(5):
    print(f'Veículo {1+i}')
    carros.append([input("Nome: ")])
    v.append(float(input("Km por litro: ")))

for i in range(5):
    print(f"""{i+1} - {carros[i]} - {v[i]:.2f} Km/L - {1000/(v[i])} L p/ 1000 KM - R$ {(1000/(v[i]))*gas}""")