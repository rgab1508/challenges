for i in range(35163):
    n = input().split(" ")

    if n[0] == "X":
        print("X")
    else:
        n.reverse()
        print(" ".join(n))