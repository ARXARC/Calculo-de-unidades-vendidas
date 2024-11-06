P1 = float(input("P1: "))
P2 = float(input("P2: "))
ganancia = float(input("G: "))
unidades_T = float(input("UT: "))
unidades_P1=(P2*unidades_T-ganancia)/(-P1+P2)
unidades_P2=unidades_T-unidades_P1
print(unidades_P1)
print(unidades_P2)
