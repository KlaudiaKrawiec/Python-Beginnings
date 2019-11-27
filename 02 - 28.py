x = 1
while(not (x % 7 == 0 and
           x % 2 == 1 and
           x % 3 == 1 and
           x % 4 == 1 and
           x % 5 == 1 and
           x % 6 == 1)):
    x += 1
print(x)