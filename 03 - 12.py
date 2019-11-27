tab = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]

file = open("imoina i nazwiska.txt", "w")

file.write("Imie,Nawisko,Email\n")

for ind in tab:
    for x in ind:
        y = ind.index(x)
        if y<2:
            file.write(f"{x},")
        else:
            file.write(f"{x}\n" )
file.close()