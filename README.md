Instructivo del Código y Algoritmo

Propósito: Calcular la cantidad de unidades de dos productos (P1 y P2) que se deben producir para obtener una ganancia determinada, dado el precio de cada producto y el total de unidades que se pueden producir.

Variables:

P1: Precio del producto 1
P2: Precio del producto 2
G: Ganancia deseada
UT: Total de unidades que se pueden producir
unidades_P1: Cantidad de unidades del producto 1 que se deben producir
unidades_P2: Cantidad de unidades del producto 2 que se deben producir
Algoritmo:

Entrada de datos:
Solicitar al usuario que ingrese el precio del producto 1 (P1)
Solicitar al usuario que ingrese el precio del producto 2 (P2)
Solicitar al usuario que ingrese la ganancia deseada (G)
Solicitar al usuario que ingrese el total de unidades que se pueden producir (UT)
Cálculo de unidades:
Calcular la cantidad de unidades del producto 1 que se deben producir (unidades_P1) utilizando la fórmula: (P2 * UT - G) / (-P1 + P2)
Calcular la cantidad de unidades del producto 2 que se deben producir (unidades_P2) restando la cantidad de unidades del producto 1 del total de unidades que se pueden producir: UT - unidades_P1
Salida de resultados:
Imprimir la cantidad de unidades del producto 1 que se deben producir (unidades_P1)
Imprimir la cantidad de unidades del producto 2 que se deben producir (unidades_P2)
