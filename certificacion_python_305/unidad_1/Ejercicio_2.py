try:
    alumnos=["Vaneza","Emanuel","Monserat","Julio","Paola","Rosalia","Fransisco","Adriana","Maximiliano","juan"]
    print(alumnos)
    alumnos.append("Vaneza")
    print(alumnos[1])
    alumnos[1]=("emanuel")
    print(alumnos[2])
    alumnos.remove("Monserat")
    print(alumnos[3])
    alumnos.append("Julio")
    print(alumnos[4])
    alumnos[2]=("Paola")
    print(alumnos[5])
    alumnos.remove("Rosalia")
    print(alumnos[6])
except ImportError:
    print("Indice incorrecto")