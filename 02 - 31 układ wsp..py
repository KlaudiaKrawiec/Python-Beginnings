x =  4
y = -1

if x == 0 and y == 0:
    print(f'Punkt P znajduje się na początku układu wsp. P = ({x},{y})')
elif x>0 and y>0:
    print('Pierwsza ćwiartka')
elif x<0 and y<0:
    print('Trzecia ćwiartka')
elif x == 0 and (y<0 or y>0):
    print('P znajduje się na wsp. y ')
elif (x>0 or x<0) and y==0:
    print('P znajduje się na wsp. x ')
elif x>0 and y<0:
    print('Druga ćwiartka')
elif x<0 and y>0:
    print('Czwarta ćwiartka')
    