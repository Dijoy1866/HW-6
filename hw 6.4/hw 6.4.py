# Вывести треугольник #4 с шириной N с помощью цикла while

N = int(input("Please input number :"))
i = N
d = '*'
s = N
p = ' '
print(d * i)
while s != 1:
    s -= 1
    i -= 1
    print(p * (N-i) + d * i)



#for line_number in range(1,number_of_lines+1):
 #     print(" "* (number_of_lines-line_number) + "*"*line_number)


#  print(i**2); i = i * 10 + 1