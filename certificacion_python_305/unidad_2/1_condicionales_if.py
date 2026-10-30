edad=int(input("Introduce tu edad"))
if edad <= 0 and edad <= 3:
    print("ERES BEBE")
elif edad >= 0 and edad <= 11:
     print("ERES UN NIÑO")
elif edad >= 12 and edad <= 18:
     print("ERES UN ADOLESENTE")
elif edad >= 18 and edad <= 29:
     print("ERES UN JOVEN")
elif edad >= 30 and edad <= 40:
     print("ERES UN CHAVO-RUCO")
elif edad >= 41 and edad <= 100:
     print("ERES UN ADULTO")
else:
    print("ESTAS ROBANDO OXIGENO")

