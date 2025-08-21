prices = [7,1,5,3,6,4]

min=float('inf')
max=0

for price in prices:
    if prices[price]<min:
        min=prices[price]
    elif (prices[price]-min)>max:
        max=prices[price]-min
print(max)