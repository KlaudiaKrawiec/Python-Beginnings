
tab = [32, 16, 5, 8, 24, 7]

f = open('tab.txt', 'w')

for x in tab:
    i = str(x)
    f.write(f'{i} \n')
    
    
f.close()