

# def add_num(number,result):
    # while(number>10):
    #     digit=number%10
    #     result+=digit
    #     number=number//10
    # if (result<=9):
    #     print(result)
    # else:
    #     add_num(result,0)
inp= 1632791
if (inp<=9):
    print(inp)
else:
    # add_num(inp,0)
    number=inp
    result=0
    while(number>0):
        digit=number%10
        result+=digit
        number=number//10
        if (result>9):
            result=(result%10)+(result//10)
    if (result<=9):
        print(result)
    else:
        # add_num(result,0)
        number=result