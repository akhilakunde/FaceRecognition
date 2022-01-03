Num = 5                                                     NOTE: here num we can keep our own number to get the output
Factorial = 1
if Num < 0:
    print("factorial doesn't exist for -ve numbers")
elif Num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, Num + 1):
        Factorial = Factorial * i
    print("The factorial of",Num,"is",Factorial)
