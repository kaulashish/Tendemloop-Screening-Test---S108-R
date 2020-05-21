ar=list(filter(lambda x: x%7==0 and x%5==0, range(1500, 2701)))
print(*ar, sep=', ')