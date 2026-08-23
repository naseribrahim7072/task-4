temp = float(input("Enter the temperature in Celsius: "))
fahrenheit = temp * 9/5 + 32
print("The temperature is", fahrenheit, "Fahrenheit")
if temp > 30:
    print("It's a hot day")
elif temp < 15:
    print("It's a cold day")
else:
    print("It's normal")