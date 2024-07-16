def computepay(hrs, rate):
   
    if (hrs > 40):
        pay = (40 * rate) + (hrs - 40) * (1.5 * rate)
    else:
        pay = hrs * rate
        
    return pay
  
  
hrs = input("Enter Hours:")
rate = input("Enter rate:")
fh = float(hrs)
fr = float(rate)  
xp = computepay(fh, fr)
print("Pay", xp)        
