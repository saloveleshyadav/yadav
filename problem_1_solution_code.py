a = 1
b = 0
while True:
    if a > 999:
        break
    else:
        if a % 3 == 0 or a % 5 == 0:
            b = a+b
    a = a+1
print(b)