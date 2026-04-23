for i in range(5) :
    for x in range(5) :
        if i == 0 or i == 4:
            print("*", end=" ")
        elif x == 0 or x == 4:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()