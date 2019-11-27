
file = open("NoEducation.txt","r")


for x in file:
    print(f'{len(x)} {x}', end='')
    
file.close()