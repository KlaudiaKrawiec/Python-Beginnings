from random import randrange

list = []
for i in range(1,7):
    number = randrange(1,101)
    list.append(number)
    
print('Tablica nieposeortowana',list)

lenght = len(list)

for x in range(lenght):
       # ost = lenght - 1 #zaczynamy od ostatniej kom
    for ost in range(lenght - 1 ,0,-1):   #while ost > x:
        if list[ost] < list[ost - 1]:  #zamiana = zam
            zam = list[ost]
            list[ost] = list[ost - 1]
            list[ost - 1] = zam
                                   #ost -= 1
print('Tablica posortowana',list)
            

