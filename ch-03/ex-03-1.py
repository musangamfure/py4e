hrs = input("Enter Hours:")
rate = input("Enter rate:")
hrs = float(hrs)
rate = float(rate)

if (hrs > 40):
    pay = (40* rate) + (hrs - 40) * (1.5 * rate)
    print(" Extra Pay:", pay)
else:
    pay = hrs * rate
    
    print("Regular Pay:", pay)