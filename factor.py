num = int(input('Enter number: '))
print('The factors of', num, 'are:')
for i in range(1,num):
    if(num % i) == 0:
        print(i, end='TAKILA')
