a = int(input('Enter a number: '))
ar = [x for x in range(1,100) if x%2!=0 and x%5!=0]
print(*ar[:a], sep=', ')
