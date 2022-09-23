# Вывести треугольник #3 с шириной N с помощью цикла while

N = int(input("Please input number :"))
i = N
d = '*'
s = N
p = ' '
print(d * i)
while s != 1:
    s -= 1
    i -= 1
    print(p * (N-i) + (d * i))


