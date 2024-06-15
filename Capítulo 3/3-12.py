x_segundos = int(input("Digite os segundos: "))

horas = x_segundos // 3600
minutos = x_segundos % 3600 // 60
segundos = x_segundos % 60

print('{0}h{1}m{2}s'.format(horas, minutos, segundos))