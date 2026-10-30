 #el mapa del tesoro 
mapa=[
    [".",".",".","."],
    [".",".","B","."],
    [".",".",".","."],
    [".",".","A","."]
]
filas=len(mapa)
columnas=len(mapa)
#recorriendo la matriz con ciclo animado 
#ciclo externo para manejar filas (i)
for i in range(filas):
    #ciclo interno para manejar columnas (j)
    for j in range(columnas):
      #Verificamos si encomtramos el tesoro
      if mapa[i][j]=="A":
        print(f"Tesoro encontrado el la posicion [{i}][{j}]")
      if mapa[i][j]=="B":
        print(f"Tesoro encontrado el la posicion [{i}][{j}]")