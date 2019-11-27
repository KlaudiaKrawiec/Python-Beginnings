import re #WYRAŻENIA REGULARNE

str = "MAT Matematyka 45 \nGEO Geografia 210 \nHIS Historia 28 \nINF Informatyka 196"

# Kod PRZEDMIOTU

kod = r"^\D{3} "

# Nazwa przedmiotu

nazwa = r" [a-zA-Z]*"

# Liczba uczestników

uczestnicy = "\d+"

match_kod = re.search(kod,str)
match_nazwa = re.search(nazwa,str)
match_uczestnicy = re.search(uczestnicy,str)

if match_kod:
    print(match_kod.group())
if match_nazwa:
    print(match_nazwa.group())
if match_uczestnicy:
    print(match_uczestnicy.group())