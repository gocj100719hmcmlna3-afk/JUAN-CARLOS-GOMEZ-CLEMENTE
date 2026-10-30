try:
    #Ejemplo 1 sin manejo de excepciones
    numero1=float(input("Ingresa el primer numero"))
    numero2=float(input("ingresa el segundo numero"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("DIVICION ENTRE CERO FALLIDA")
except ValueError:
    print("SOLO INTRODUCE NUMEROS")