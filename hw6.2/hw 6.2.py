# Вывести треугольник #2 с шириной N с помощью цикла while

N = int(input("Please input number :"))

h = 1


while h <= N:
    w = 1
    while w <= h:
        print("*", end=" ")
        w += 1
        h += 1
    print()

