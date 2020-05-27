print('Enter numbers separated by space: ')
ar = list(map(int, input().strip().split()))
even=0
odd=0
for i in range(len(ar)):
    if ar[i]%2==0:
        even+=1
    else:
        odd+=1
print('even: {}'.format(even))
print('odd: {}'.format(odd))
