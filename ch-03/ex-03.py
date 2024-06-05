hours = input("How many hours did you work today? ")
rate = input("What is your hourly rate? ")

hours = float(hours)
rate = float(rate)

pay = hours * rate

print("You earned $" + str(pay))

