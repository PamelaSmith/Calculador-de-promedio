num = int(raw_input("Digite un numero para encontrar el factorial : "))
n = 1
while num >= 1:
    n = n * num
    num -= 1
print "El factorial del numero introducido es ",n
