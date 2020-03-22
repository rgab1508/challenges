t = int(input())

for it in range(t):
    n, k, p = map(int, input().split(" "))
    stack = []
    plates = []
    for i in range(n):
        a = list(map(int, input().split(" ")))
        stack.append(a)
        plates = []
        curr_best_plate = None
        for i in range(len(stack)):
            for j in range(len(stack[i])):
                if stack[i][0]>stack[j][0]:
                    curr_best_plate = [stack[i][0],i]
                else:
                    curr_best_plate = [stack[j][0], j]
                plates.append(curr_best_plate[0])
                stack[curr_best_plate[1]].pop(0)
            
        print(plates)