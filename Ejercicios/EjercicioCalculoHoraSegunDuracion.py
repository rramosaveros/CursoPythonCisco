hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

sumaMinDura = int(min + dura)
divDuraMasMin = int(sumaMinDura / 60)
sumaHoraMasDiv = int(hora + divDuraMasMin)
hora2 = int(sumaHoraMasDiv % 24)
min2 = int(sumaMinDura % 60)
# coloca tu código aqui
print(str(hora2)+ ":" + str(min2)) 