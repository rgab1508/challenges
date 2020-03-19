n = int(input())

body = [0, 0, 0]
# forces = []

for i in range(n):
    force = list(map(int, input().split(" ")))
    # forces.append(force)
    body[0] += force[0]
    body[1] += force[1]
    body[2] += force[2]


if body == [0, 0, 0]:
    print("YES")
else:
    print("NO")