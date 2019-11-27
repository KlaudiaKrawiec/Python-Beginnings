
for x in range(1,51):
    if x%3 == 0 and x%5 == 0:
        x = 'BINGO'
        print(x)
    elif x%3 == 0:
        x = 'BIM'
        print(x)
    elif x%5 == 0:
        x = 'BAM'
        print(x)
    
    else:
        print(x)
    