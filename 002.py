a = 1
b = 2

_sum = 2

while b < 4000000:
    temp = b
    b += a
    a = temp
    if b % 2 == 0:
        _sum += b

print(_sum)
