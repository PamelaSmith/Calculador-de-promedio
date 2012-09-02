nu = int(raw_input('Cuantos numeros? '))

su = 0.0
for i in range(nu):
    x = float(raw_input())
    su = su + x

prom = su / nu
print 'El promedio es' , prom
