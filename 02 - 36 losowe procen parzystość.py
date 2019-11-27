from random import randrange

def los():
    x = randrange(1,51)
    
    return x

list_p=[]
list_n=[]
print('Dla 1000 liczb losowych z przedziału:')
for y in range(1000):
    x = los()
    if x%2 == 0:
        list_p.append(x)
    else:
        list_n.append(x)

p = len(list_p)
procent_p = (p/1000)*100
print(f'Liczby parzyste: {procent_p}%')
n = len(list_n)
procent_n = (n/1000)*100
print(f'Liczby nieparzyste: {procent_n}%')