
tab1 = [3,5,6,2,1,7]
tab2 = [8,7,4,9,3,4]
tab3 = []

n = len(tab1)

for x in range(n):
    y = tab1[x] + tab2[x]
    tab3.append(y)
    
print(f"{tab1} + {tab2} = {tab3}",end = " ")