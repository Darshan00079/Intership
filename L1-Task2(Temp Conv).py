def temperature_to_Celsius(Fahrenheit):
    return (Fahrenheit-32)*5/9

def temperature_to_Fahrenheit(Celsius):
    return (Celsius* 9/5)+32

print('''********Welcome to Temperature Convertor System********''')
print('''
        _________________
      ._)               (_.
      |    °F  ,-. °C     |
      |        | |___ 40  |
      | 100 ---| |        |
      |        | |        |
      |  90 '' | |___ 30  |
      |  80 ___| |        |
      |        | |        |
      |  70 ---| |___ 20  |
      |        | |        |
      |  60 '' | |        |
      |  50 ___| |___ 10  |
      |        | |        |
      |  40 ---| |        |
      |        |_|___ 0   |
      |  30 '' | |        |
      |  20 ___| |        |
      |        | |___-10  |
      |  10 ---| |        |
      |        | |        |
      |   0 '' | |___-20  |
      | -10 ___| |        |
      |        | |        |
      | -20 ---| |___-30  |      
      |        |#|        |
      | -30 '' |#|        |
      | -40 ___|#|___-40  |      
      |        |#|        |
      |        |#|        |
      |       (###)       |
      |_       `-'       _|   
      ' )_______________( '
''')
temperature=int(input("Enter the temperature: "))
temperature_unit=input("Enter the unit of temperature(C for Celsius and F for Fahrenheit): ").upper()

if temperature_unit=='C':
    print(f"{temperature}°C in Fahrenheit is :",temperature_to_Fahrenheit(temperature),"°F")
elif temperature_unit=='F':
    print(f"{temperature}°F in Celsius is:",temperature_to_Celsius(temperature),"°C")
else:
    print("Sorry! Please enter the valid input")
