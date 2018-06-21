n = eval(input('input any number: '))
sign = 1
pi = 0
for i in range(1, n+1, 2):
    for n in range(3, n+1, 4):
        n *= -1
    sign = 4 / i
    pi += sign


print(pi)
