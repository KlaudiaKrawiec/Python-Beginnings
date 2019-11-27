
produkty = []
ilosc = int(input("Podaj ilość produktów:"))
suma = 0

while len(produkty)<ilosc:  
    y = int(input(f"Wprowadź cene produktu:"))
    produkty.append(y)

for x in range(ilosc):
    suma += produkty[x]

kwota = int(input("Wprowdź pieniądzę do kasy:"))

if kwota<suma:
    print("Za mała kwota!")
elif kwota == suma:
    print("Przyjęto zapłatę. Dziękujemy i zapraszamy ponownie! ")
elif kwota>suma:
    reszta = kwota - suma
    il50 = reszta//50
    il20 = (reszta - il50*50)//20
    il10 = (reszta - il50*50 - il20*20)//10
    il5 = (reszta - il50*50- il20*20 - il10*10)//5
    il2 = (reszta - il50*50- il20*20 - il10*10 - il5*5)//2
    il1 = (reszta - il50*50- il20*20 - il10*10 - il5*5 - il2*2)//1
    print(f"Wydaję resztę: {il50}x50zł {il20}x20zł {il10}x10zł {il5}x5zł {il2}x2zł {il1}x1zł = {reszta}")