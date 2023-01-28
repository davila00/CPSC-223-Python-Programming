import weather
import calendar

filename = "w.dat"
data = weather.read_data(filename)

while (True):
    print("\n\t\t***TUFFY TITATN WEATHER LOGGER MAIN MENU***\n")

    print("1. Set data filename \n2. Add weather data \n3. Print daily report")
    print("4. Print historical report \n9. Exit the program")
    choice = int(input("\nEnter Menu Choice: "))

    if choice == 1:
        newfile = input("Enter data filename: ")
        filename = newfile

    elif choice == 2:
        date = input("Enter date (YYYYMMDD): ")
        time = input("Enter time (hhmmss): ")
        temperature = int(input("Enter temperature: "))
        humidity = int(input("Enter humidity: "))
        rainfall = float(input("Enter rainfall: "))

    elif choice == 3:
        date = input("Enter date (YYYYMMDD): ")
        time = weather.report_daily(date)
        print(time)

    elif choice == 4:
        historical = weather.report_historical(data)
        print(historical)

    elif choice == 9:
        break
