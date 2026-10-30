colores=["azul","Morado","ROJO","Amarillo","Verde"]
color=input("Ingresa el color: ")#Naranja
encotrado=False
for contador in colores:
    print(colores)
    #si el color actual es "ROJO," detener el bicle
    if contador== color: 
        print("color encontrado1 saliendo del bicle ")
        encotrado = True
        break
if not encotrado:
    print("el color,",)