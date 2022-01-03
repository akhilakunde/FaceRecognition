print("Enter a range in numbers:")
R1=int(input())
R2=int(input())
print(R1," to ",R2," palindrome numbers are ");
for i in range(R1,R2+1):
   A=i
   B=0
   while(A!=0):
      rem=A%10
      A=int(A/10)
      B=B*10+rem
   if(i==B):
      print(i,end=" ")
