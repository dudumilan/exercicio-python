n = 1
n1 = 0
n2 = 0
n3 = 0
n4 = 0
while n > 0:
    n = int(input())
    if n > 0 and n <= 25:
        n1 += 1
    elif n > 25 and n <= 50:
        n2 += 1
    elif n > 50 and n <= 75:
        n3 += 1
    elif n > 75 and n <= 100:
        n4 += 1
print(f'números no intervalo [0-25]: {n1}')
print(f'números no intervalo [26-50]: {n2}')
print(f'números no intervalo [51-75]: {n3}')
print(f'números no intervalo [76-100]: {n4}')
