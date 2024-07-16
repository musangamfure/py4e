list = [9, 12, 20, 34, 40, 5, 63, -7, 88, 10,3]

smallest =None
for i in list:
    if smallest is None:
        smallest = i
        print(" Current Smallest:", smallest)
    elif i < smallest:
        smallest = i
    print("Finanl:",smallest)