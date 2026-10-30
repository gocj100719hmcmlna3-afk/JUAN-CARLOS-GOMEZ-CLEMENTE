try:
    numero1=float(input("Ingresa el primer numero"))
    numero2=float(input("ingresa el segundo numero"))
    resultado=numero1/numero2
except ValueError:
    print("solo intruduce numeros")
except ZeroDivisionError:
    print("Divicion entre cero")
else:
    print("El resultado es ",resultado)
finally:
    print("Programacion finalizado")