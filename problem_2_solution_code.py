def fib():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first+second
        if first > 4000000:
            break


total = 0
for i in fib():
    if i % 2 == 0:
        total = i+total

print(total)
