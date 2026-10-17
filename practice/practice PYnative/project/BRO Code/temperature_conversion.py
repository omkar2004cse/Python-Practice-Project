# temperature conversion
temp=float(input("Enter a Temperature:-"))
unit=input("unit of Temperature (C or F):-")
if unit=='C':
    print("Temperatur in Fehrenheit is:-",round((temp*9)/5+32,2))
elif unit=="F":
    print("Temperature in Celsius is:-",round((temp-32)*5/9,2))
else:
    print(unit,"is not Valid")