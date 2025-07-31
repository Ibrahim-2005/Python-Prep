compliment= ~5             # It gives ~x = -(x+1)
And= 3&2                   # 3= 011     2=010       And=(and logic is done for both and convert) = 010 which gives us 2
Or= 3|2                    # 3= 011     2=010       Or=(or logic is done for both and convert) = 011 which gives us 3
Not= 3^2                   # 3= 011     2=010       Not=(it gives '1' for different bit and '0' for same) = 001 which gives us 1
Right_shift= 3>>2          # 3= 011     x>>y it moves the decimal point 'y' times to left that becomes 0.11 which gives us 0
Left_shift= 3<<2           # 3= 011     x<<y it moves the decimal point 'y' times to right that becomes 01100 which gives us 12


print(compliment)
print(And)
print(Or)
print(Not)
print(Right_shift)
print(Left_shift)