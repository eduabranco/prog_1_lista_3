from ast import While


nvl1=nvl2=nvl3=nvl4=0
while True:
    x=float(input("Insira um número(Para Encerrar, insira um número negativo)\n"))
    if x<0: 
        print("Número negativo inserido. Encerrando...")
        exit()
    elif x>=0 and x<=25:nvl1+=1
    elif x>=26 and x<=50:nvl2+=1
    elif x>=51 and x<=75:nvl3+=1
    elif x>=76 and x<=100:nvl4+=1
    print(f"""
            Intevalo [0-25] :{nvl1}\n
            Intevalo [26-50] :{nvl2}\n
            Intevalo [51-75] :{nvl3}\n
            Intevalo [76-100] :{nvl4}\n
            """)