
lenguage = ["Java","Python","JavaScript","C++","C#","Ruby","Perl","PHP","C","Android"]
value = [61,47,37,32,26,18,14,14,9,7]


def chart(tab1,tab2):
    #for x in tab1:
        #print(f"{x:10}:")
    lenght = (len(tab1))
    for x in range(lenght):
        y = tab2[x]*"#"
        print(f"{tab1[x]:10}:{y}")
        
        
#def value(tab):
    #for y in tab:
        #print(y*"#")
        
        
chart(lenguage,value)
