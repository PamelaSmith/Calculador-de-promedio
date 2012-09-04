nu = int(raw_input('Cuantas notas son? '))
print 'Digite las notas: '

su = 0.0
for i in range(nu):
    x = float(raw_input())
    su = su + x

prom = su / nu
print 'El promedio de las notas es ', prom
