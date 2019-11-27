
suma_p = 0
suma_n = 0

for x in range(1,51):
    if x%2 == 0:
        suma_p += x
    else:
        suma_n += x

 #suma = (1+49)*25/2 == 625
print('Suma liczb parzystych z przedziału <1,50> :' , suma_p)
print('Suma liczb nieparzystych z przedziału <1,50> :' , suma_n)

