import sys
t = int(sys.stdin.read())
for i in range(t):
    l1 = input().split(" ")
    a, b = int(l1[0]), int(l1[1])
    n = int(input())
    guess = int((a + b)/2)
    print(guess)
    sys.stdout.flush()
    ans = input()
    i=0
    while(ans != "CORRECT" and (i != n)):
        if ans == "TOO_BIG":
            guess = int((a+guess)/2)
        if ans == "TOO_SMALL":
            guess = int((guess+b)/2)
            
        print(guess)
        sys.stdout.flush()
        i+=1
        ans = input()