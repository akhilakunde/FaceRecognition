num=int(input("Enter any number:"))
A=num
akhila=0
while(num>0):
    Krishna=num%10
    akhila=akhila*10+Krishna
    num=num//10
if(A==akhila):
    print("The {0} number is palindrome".format(A))
else:
    print("Not a palindrome")