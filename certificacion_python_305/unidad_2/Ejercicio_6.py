#creando una matriz
matriz=[
    ['A','B','C','D','E'],#Filas 25 x 5 columnas 
    ['F','G','H','I','J'],#Filas 25 x 5 columnas 
    ['K','L','Ñ','O','P'],#Filas 25 x 5 columnas 
    ['Q','R','S','T','U'],#Filas 25 x 5 columnas 
    ['V','W','X','Y','Z'],#Filas 25 x 5 columnas 
]

filas=len(matriz)
columnas=len(matriz[0])

for A in range(0,5):
  
    for Z in range(0,5):
        print(f"pocicion[{A}][{Z}]={matriz[A][Z]}")
