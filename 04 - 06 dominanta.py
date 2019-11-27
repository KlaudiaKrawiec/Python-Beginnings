
list = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
n = len(list)

def sort(tab):
    for i in range(n):
        ost = n - 1
        while ost > i:
            if tab[ost] < tab[ost-1]:
                zam = tab[ost]
                tab[ost] = tab[ost - 1]
                tab[ost - 1] = zam
            ost -= 1
    return tab

def medi(tab):
    if n%2 == 1:
        ind_med = (n - 1)//2
        mediana = tab[ind_med]
    else:
        x = n//2
        y = (n//2)-1
        mediana = (tab[x] + tab[y]) // 2
    return mediana

def domi(tab):
    
    value = []  
    how_many = []
    for i in tab:
        if i not in value:
            value.append(i)
            how_many.append(1)
        elif i in value:
            ind = value.index(i)
            how_many[ind] += 1
   # print(how_many,value)
    
    max = 0
    indexmax = 0
    for m in range(len(how_many)): # wyszukanie największej wartości tablicy how_many oraz jej indexu
        if how_many[m] > max:
            max = how_many[m]
            indexmax = m
            
    dominanta = value[indexmax] # index maxymalnej wartości z tab how-many odpowiada wartości najczęściej występującej
    return dominanta
       
print(list)
print("Posortowana: ",sort(list))
print("Mediana: ",medi(list))
print("Dominanta: ",domi(list))     
        
    
        
        