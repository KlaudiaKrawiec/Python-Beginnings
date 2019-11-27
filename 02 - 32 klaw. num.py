
i=7
 
while i>0:
    j=i
    while j<i+3:
        print(j, end=' ')
        j+=1
    i-=3
    print()
    
for i in range(6,-1,-3):
    for j in range(1,4):
        print(f'{i+j}', end=' ')
    print()