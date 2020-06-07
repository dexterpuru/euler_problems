a = 3
b = 5

upto = 1000

# for this we need to add series of 3, 6, 9...; 5, 10, 15... and subtract 15, 30, 45...
# as a==d sum of series = d*int(x/d)*(1+int(x/d))/2


def mul_a_b(a, b, upto):
    _sum = 0
    count = 1

    while a*count <= upto or b*count <= upto:
        if a*count <= upto:
            _sum += a*count
        if b*count <= upto:
            _sum += b*count
        count += 1

    return _sum


print(mul_a_b(a, b, upto))
