def KelvinToFahrenheit(temp): #Asercja - zwraca true or false, if false przerywa działenie programu i wyświetla AssertionError + podany komunikat
    assert temp >= 0, "Colder than absolute zero!" 
    return ((temp-273)*1.8)+32

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
print(KelvinToFahrenheit(-5))