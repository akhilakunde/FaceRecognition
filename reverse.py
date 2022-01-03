n=int(input("Enter number: "))
rev=0
while(n>0):
    A=n%10
    rev=rev*10+A
    n=n//10
print("Reverse of the number:",rev)




NOTE : rev specifies reverse and n is giving input values like 123 or some other numbers
        A is taking a sample alphabet and n%10 defines input value % 10
        REV * 10 + A defines reverse of a number which is given by input value and multiplies by 10 + A is the solved value of upper A Ans
        n = n//10 means  the given input  which we give the number and it reverses double times // as mentioned so that's why 
                    it will get reverse order when we give the correct input 
         and finally it prints the output            