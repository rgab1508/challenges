import random
n = 1000000
s = ""
for i in range(n):
    if random.random() > 0.5:
        s += "("
    else:
        s += ")"

f = open("q_a.in", "w")
f.write("{}\n".format(str(n)))
f.write(s)
f.close()