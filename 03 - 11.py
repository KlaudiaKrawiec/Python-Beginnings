
file  = open("potegi.txt","w")



for x in range(1,11):
    file.write("{0:2d} {1:3d} {2:4d}\n".format(x,x**2,x**3))
    


file.close()

file  = open("potegi.txt","r")

file.read()
file.close()
