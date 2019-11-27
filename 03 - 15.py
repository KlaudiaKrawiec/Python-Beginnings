import re

file = open("txt.txt","r")

read = file.read()

wiek = r"[0-3][0-9]"

lines = read.split()
tab_file= []
for i in lines:
    tab_file.append(i.split(","))

for x in tab_file:
    for y in x:
        if re.match(wiek,y):
            x.remove(y)
            for j in x:
                print(j, end="  ")
            print()
file.close()