carrito=[]#lista vacia 
n_producto=int(input("Ingresa el numero de productos"))
for i in range(n_producto):
    producto=input("Ingresa el producto a tu carrito ")
    carrito.append(producto)
print("lista creada correctamente")
print(f"tu carrito contiene{carrito}")

