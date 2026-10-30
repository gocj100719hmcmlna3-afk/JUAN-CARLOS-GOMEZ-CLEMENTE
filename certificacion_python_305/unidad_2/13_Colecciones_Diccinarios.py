#creando un diccionario en python
persona={
    "nombre":"Sofia",
    "edad":28,
    "Profecion":"ingenira",
    "estidiante":False
}
print(persona)
#Accediendo a un valor en especifico
print(persona["Profecion"])
#se puede usar metodo .get() .set()
#es util proqie no marca error si si la clave 
print(persona.get("edad"))
#Modifica un volor existente
persona["edad"]=29
print(persona.get("edad"))
#Agregar un par(clave:valor)
persona["ciudad"]="san pepe ranch"
print(persona)
#Rescorre un dicci
for clave,valor in persona.items():
    print(f"{clave}:{valor}")