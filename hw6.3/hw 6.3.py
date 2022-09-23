# Вывести треугольник #3 с шириной N с помощью цикла while

N = int(input("Please input number :"))
i = N

print(('*') * i)
while i != 1:
    i -= 1

    print((' ') * (N-i) + (('*') * i))


