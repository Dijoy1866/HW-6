N = int(input("Please input number :"))

num_height = 1


while num_height <= N:
    num_width = N
    while num_width >= num_height:
        print("*", end=" ")
        num_width -= 1
    num_height += 1
    print()

