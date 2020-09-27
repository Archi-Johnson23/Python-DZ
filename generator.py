def generator():
    while True:
        for k in range(1, 1000):
            yield k
g = generator()
for i in range(1, 1000):
    print(next(g))

def foo(count):
    total = 0
    numbers = []
    while total < count:
        r = next(g)
        if r % 3 == 0 :
            numbers.append(r)
            total += 1
    return numbers
print(foo(1000))
