while True:
    celsius = float(input("\nEnter temperature in Celsius (or -999 to quit): "))
    if celsius == -999:
        print("Goodbye!")
        break
    fahrenheit = float((celsius * 9/5)  + 32)
    kelvin = float(celsius + 273.15)

    print(f"Celsius: {celsius}°C")
    print(f"Fahrenheit:  {fahrenheit}°F")
    print(f"Kelvin: {kelvin}K")

    if celsius < 0:
        print("Condition: ❄️ Freezing")
    elif celsius <= 15:
        print("Condition: 🧥 Cold")
    elif celsius > 15 and celsius < 25:
        print("Condition: 😊 Warm")
    else:
        print("Condition: ☀️ Hot")       





