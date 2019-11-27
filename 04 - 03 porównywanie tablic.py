
def sim(tab1, tab2):
    len1 = len(tab1)
    len2 = len(tab2)
    if len1 == len2:
        for x in range(len1):
            if tab1[x] != tab2[x]:
                return False
    else:
        return False
        
    return True
    
list1 = [1,2,3,4]
list2 = [1,2,3,4]
list3 = [2,5,6]
list4 = [5,6,6]

print(sim(list1,list2))
print(sim(list2,list3))
print(sim(list4,list1))