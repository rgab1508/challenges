t = int(input())

for it in range(t):
    s = input()
    s += "X"
    n = len(s)
    d = n

    for i in range(d):
        step = 0

        for _s in s:
            if _s == "R":
                step += 1
            elif _s == "L":
                step -= 1
            if _s == "X":
                break   

        if step > n:
            continue

    
    print(f"{i}: {step}")
