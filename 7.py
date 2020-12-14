def generator():
    i = 1
    for el in range(1, n+1):
        i = i * el
        yield i

n = 7

g = generator()

for el in g:
    print(el)