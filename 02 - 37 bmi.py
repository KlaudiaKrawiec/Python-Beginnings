
def bmi(x,y):
    BMI = masa/(wzrost**2)
    print('Twoje BMI to: ', BMI)
    return BMI
    
def check(b):
    if b>18.5 and b<24.99:
        print('Współczynnik poprawny')
    else:
        print('Wspólczynnnik niepoprawny')
    
masa = int(input('Wprowadź swoją mase ciała (w kg): '))
wzrost = float(input('Wprowadź swój wzrost (w m): '))
    
check(bmi(masa,wzrost))

