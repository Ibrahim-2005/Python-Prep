p=int(input("Principle:"))
r=float(input("Rate of intrest:"))
n=int(input("Years:"))
com=int(input("How many times compounded:"))
intrest=p * (1 + r / 100) **n
print("Intrest is ",round(intrest,2))