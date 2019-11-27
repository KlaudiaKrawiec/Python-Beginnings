
my_tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def pick(tab):
    for x in tab:
        if type(x) == int:
            yield x
        else:
            for y in pick(x):
                yield y
def sum(tab):
    sum = 0
    for i in tab:
        sum += i
    return sum

allValue = list(pick(my_tab))

suma = sum(allValue)

print(allValue)
print("Suma elementów:", suma)