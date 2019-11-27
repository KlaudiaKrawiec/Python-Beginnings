from random import randrange as r

def sumacyfr(n):
    if n==0:
        return n
    else:
        return (n%10) + sumacyfr(n//10)
        

wymiar = r(10)

tab = [r(1001) for x in range(wymiar)]

print(tab)

sumacyfrwtab = 0

for x in tab:
    y = sumacyfr(x)
    sumacyfrwtab += y

print(f"Suma cyfr w tablicy {sumacyfrwtab}")