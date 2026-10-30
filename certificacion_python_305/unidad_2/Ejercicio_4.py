promedio=[9,10,6,5,7]
#1. Encontrar el promedio mas bajo y el moyor  usando ciclo for 
# suponemos inicialmente que el promedio mas bajo es el primer elemento 
promedio_bajo=promedio[0] 
for contador in promedio:
    if contador<promedio_bajo:
        promedio_bajo=contador
print(promedio_bajo)

promedio_mayor=promedio[0] 
if contador>promedio_mayor:
        promedio_mayor=contador
print(promedio_mayor)