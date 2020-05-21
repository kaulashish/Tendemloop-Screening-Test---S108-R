a = int(input('Enter a number: '))
ar = [x for x in range(1,a+1)]
for i in range(0,a+1):
    if i%2==0:
        x=ar[:i]
        print(*x[::-1], sep=' * ')
    else:
        print(*ar[:i], sep=' * ')