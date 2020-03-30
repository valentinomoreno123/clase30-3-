num = int(input("Introduce la altura de un triángulo : "))
for a in range(1, num+1, 2):
    for b in range(a, 0, -2):
        print(b, end=" ")
    print("")