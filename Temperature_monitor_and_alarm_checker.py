
# ==========================================
# TEMPERATURE MONITOR AND ALARM CHECKER
# CTE123 PYTHON MINI PROJECT
# ND1 MECHATRONICS ENGINEERING
# ==========================================

# Function to monitor machine temperatures
def temperature_monitor():

    readings = []  # Stores the five temperature readings

    safe_limit = 80.0  # Maximum safe temperature in Celsius

    print("\n===================================")
    print("   MACHINE TEMPERATURE MONITOR")
    print("===================================")

    print("Enter five temperature readings.")
    print("All readings must be in Celsius.\n")

    # Loop to collect five temperature readings
    for i in range(5):

        while True:
            try:
                temperature = float(
                    input(f"Enter temperature reading {i + 1}: ")
                )

                # Check that temperature is not negative
                if temperature < 0:
                    print("Invalid reading! Temperature cannot be negative.")
                else:
                    readings.append(temperature)
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

    # Calculate highest, lowest and average temperatures
    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    # Display the temperature results
    print("\n========== TEMPERATURE REPORT ==========")

    print(f"Readings: {readings}")
    print(f"Highest temperature: {highest:.2f} °C")
    print(f"Lowest temperature: {lowest:.2f} °C")
    print(f"Average temperature: {average:.2f} °C")

    # Check for overheating
    print("\n========== MACHINE STATUS ==========")

    if highest > safe_limit:
        print("WARNING! MACHINE OVERHEATING!")
        print("ALARM: Temperature has exceeded the safe limit.")

    elif highest >= 70:
        print("CAUTION! Machine temperature is approaching the safe limit.")

    else:
        print("NORMAL: Machine is operating within the safe temperature range.")

    # Extra feature: Show individual reading warnings
    print("\n========== INDIVIDUAL READING CHECK ==========")

    for i, temp in enumerate(readings, start=1):

        if temp > safe_limit:
            print(f"Reading {i}: {temp} °C - DANGER!")

        elif temp >= 70:
            print(f"Reading {i}: {temp} °C - CAUTION!")

        else:
            print(f"Reading {i}: {temp} °C - NORMAL")


# Main program: Repeat until the user chooses to quit
while True:

    print("\n1. Start Temperature Monitoring")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        temperature_monitor()

    elif choice == "2":
        print("Thank you for using the Temperature Monitor.")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")
