#cadenas y concatenacion con (+)
cadena1='hola' 
cadena2="mundo"
multilinea="""esto es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#cadena y repeticion
eco="ja"*3
print(eco)
#cambiar una cadena de minusculas a mayuculas 
tu_nombre='juan carlos'
print(tu_nombre.upper())
#cambiar una cadena de mayosculas a minusculas
print(tu_nombre.lower())
#remplasar texto en la caden 
frase="Me guata matematicas"
print(frase.replace("programacion","matematicas"))
#formato de contanentar cadena con valor (F-string)
edad=16
Nombre="juan carlos"
mensaje=f"Hola, ma llamo {Nombre} y tengo\n{edad}años"
print(mensaje)
#contar los caracteres de una cadena
texto= "¡Felisidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si un texto contiene una palabra
oracion="Aprender python es devertido "
if "python" in  oracion:
    print("encontrado")
else:
    print("No esta")
#validar contenido de una cadena 
ncadena="aaa"
print(ncadena.isalpha())#true
print(ncadena.isdigit())#false