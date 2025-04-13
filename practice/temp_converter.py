#  Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
temp_c=float(input("enter a temperature in celsius is:-"))
temp_f=(temp_c*(9/5))+32
print("Temperature in Fahrenheit is:-",temp_f)