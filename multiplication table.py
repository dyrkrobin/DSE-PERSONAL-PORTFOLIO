while True:
    num= int(input("Enter a number greater than 1"))

    if num <1:
         break
    else:
        print("\nmMultiplication Table of", num)
        for i in range (1, 13):
            print(num, "x", i, "=", num * i)


                    
