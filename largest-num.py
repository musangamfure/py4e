list = [1,23,3,4,50,0,76,8,9,10]

lastest = -1
print("Before:", lastest)
for i in list:
    if i > lastest:
        lastest = i
    print("Current:", lastest)
print("After:", lastest)
        