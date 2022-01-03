akhila = int(input("Enter a number: "))
krishna = 0
temp = akhila
while temp > 0:
   digit = temp % 10
   krishna += digit ** 3
   temp //= 10
if akhila == krishna:
   print(akhila,"is an Armstrong number")
else:
   print(akhila,"is not an Armstrong number")