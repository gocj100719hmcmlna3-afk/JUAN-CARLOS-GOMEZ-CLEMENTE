carrito=[]
cantidad=int(input("¿cuantos productos quieres agregar al carrito"))
for contador in range(cantidad):
    producto=input(f"Ingresa el producto",{contador+1})
    carrito.append(producto)
print("\nTu lista de compra es:")
print(carrito)

#  f-string(cadena con formato) 