
def power(x,n):
    if n == 0:
        return("1")
    elif n == 1:
        return(x)
    elif n > 1:
        return x * power(x,n-1)
    
print(power(2,2))
print(power(2,3))
print(power(5,3))
print(power(4,5))
print(power(82,0))
    
    