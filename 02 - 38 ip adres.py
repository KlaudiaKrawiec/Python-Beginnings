from random import randrange as r

def a_ip():
    ip = []
    for w in range(4):
        los = r(256)
        ip.append(los)
    for k in range(1,6,2):
        ip.insert(k,'.')
    for x in ip:
        print(x,end='')
    return ip

for d in range(20):
    a_ip()
    print()



    