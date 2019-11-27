masa = int(input('Wprowadź swoją mase ciała (w kg): '))
wzrost = float(input('Wprowadź swój wzrost (w m): '))
BMI = masa/(wzrost**2)
print('Twoje BMI to: ', BMI)

if BMI < 16.0:
    print('Jesteś Wygłodzony!')
elif BMI > 16.0 and BMI <= 17.0:
    print('Jeśteś Wychudzony!')
elif BMI > 17.0 and BMI <= 18.5:
    print('Masz Niedowagę!')
elif BMI > 18.5 and BMI <= 25.0:
    print('Gratulacje! Waga w normie!')
elif BMI > 25.0 and BMI <= 30.0:
    print('Masz nadwagę!')
elif BMI > 30.0 and BMI <= 35.0:
    print('Uwaga! I stopień otyłości!')
elif BMI > 35.0 and BMI <= 40.0:
    print('Uwaga!! II stopień otyłości!!')
else:
    print('Uwaga!!! III stopień otyłości!!!')



print("Teraz znasz już swoje BMI :)")