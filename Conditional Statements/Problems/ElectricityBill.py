units=int(input("ENTER THE TOTAL UNITS CONSUMED:"))
if units <= 100:
    bill=units*1
    print("Bill is " ,bill," Rupees")
elif units >100 and units <=200:
    bill=100+((units-100)*1.5)
    print("Bill is " ,bill," Rupees")
else:
    bill=100+((100)*1.5)+((units-200)*2)
    print("Bill is " ,bill," Rupees")