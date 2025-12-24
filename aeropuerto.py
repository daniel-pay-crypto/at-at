#la libreria import random es para generar numeros aleatorios
#(en este caso generar vuelos diarios)
import random

#ahora defino variables para el numero de dias en un año y los rangos de vuelos diarios segun el tipo de dia (laboral o fin de semana)
dias_en_un_año = 365

#rangos de vuelos en dias laborales
vuelos_laborales_min = 20
vuelos_laborales_max = 40

#rango de vuelos en fines de semana
vuelos_fin_semana_min = 10
vuelos_fin_semana_max = 25

#ahora creo funcion para identificar fines de semana
#usamos % 7 ya que el modulo % devuelve el sobrante de una division y 7 por los siete dias de la semana
def es_fin_semana(dia):
    return dia % 7 in [5, 6]

#ahora simulo vuelos diarios para todo el año
vuelos_diarios = [12]

#utilizamos for para iterar dia por dia durante un año
#Traducción literal L28: Para (for) cada día (dia) en el (in) rango (range) del 0 al 364 (365 días) (dias_en_un_año), haz lo siguiente:
#for itera sobre elementos de objetos iterables (listas, tuplas, diccionarios)
#En Python, una iteración es la repetición de un bloque de código mediante estructuras de control como bucles (for o while), donde cada repetición se denomina "iteración"
for dia in range(dias_en_un_año):
    if es_fin_semana(dia):
        vuelos = random.randint(vuelos_fin_semana_min, vuelos_fin_semana_max)
    else:
        vuelos = random.randint(vuelos_laborales_min, vuelos_laborales_max)
        vuelos_diarios.append(vuelos)

#sumamos el total de vuelos  y calculamos el promedio diario
total_vuelos = sum(vuelos_diarios)
promedio_diario = total_vuelos / dias_en_un_año

#mostrar resultados en pantalla (imprimo el total anual y el promedio diario con formato claro)
print(f"total de vuelos saliendo del aeropuerto diciembre en un año: {total_vuelos}")
print(f"promedio diario de vuelos {promedio_diario:-2f}")


#no creo socio eri terrible gey