W, H = map(int, input().split(" "))

developers = []
all_developers = []
dev_desks = []
dev_desks_conf = []

pro_managers = []
all_managers = []
man_desks = []
man_desks_conf = []

comp_rate = dict()

grid = []

class Developer():
    def __init__(self, _id, comp, bp, ns, skills):
        self._id = _id
        self.comp = comp
        self.bp = bp
        self. ns = ns
        self.skills = skills
        self.placed = False
        self.desk = []


class ProjectManager():
    def __init__(self,_id, comp, bp):
        self._id = _id
        self.comp = comp
        self.bp = bp
        self.placed =False
        self.desk = []

    def __str__(self):
        return f"{self.comp}: {self.bp}"

for ih in range(H):
    l = list(input())
    grid.append(l)


ND = int(input())

for ind in range(ND):
    l = input().split(" ")
    comp = l[0]
    bp = int(l[1])
    ns = l[2]
    skills = l[3:]
    d = Developer(ind, comp, bp, ns, skills)
    developers.append(d)
    all_developers.append(d)

for i in range(len(developers)):
    if developers[i].comp in comp_rate:
        comp_rate[developers[i].comp] += 1
    else:
        comp_rate[developers[i].comp] = 1



NP = int(input())

for inp in range(NP):
    l = input().split(" ")
    comp = l[0]
    bp = int(l[1])
    pm = ProjectManager(inp, comp, bp)
    pro_managers.append(pm)
    all_managers.append(pm)

pro_managers.sort(key = lambda x: comp_rate[x.comp])
pro_managers.reverse()

for i in range(H):
    for j in range(W):
        if grid[i][j] == "M":
            man_desks.append([i, j])
        elif grid[i][j] == "_":
            dev_desks.append([i, j])

# print(man_desks, dev_desks)            

def find_and_place_man(desk):
    pm = pro_managers[0]
    pm.placed = True
    pm.desk = reversed(desk)
    man_desks_conf.append(pm)
    pro_managers.pop(0)
    return pm

def find_and_place_dev(desk):
    d = developers[0]
    d.placed = True
    d.desk = reversed(desk)
    dev_desks_conf.append(d)
    developers.pop(0)
    return d

# for i in range(len(man_desks)-1, 0, -1):
#     pm = find_and_place_man(man_desks[i])
#     man_desks.remove(i)
i = 0
while i <= len(man_desks):
    pm = find_and_place_man(man_desks[0])
    man_desks.pop(0)
    # print(man_desks)
    i+=1

# for j in range(len(dev_desks)-1, 0, -1):
#     d = find_and_place_dev(dev_desks[i])
#     dev_desks.pop()
j = 0
while j <= len(dev_desks):
    d = find_and_place_dev(dev_desks[0])
    dev_desks.pop(0)
    # print(dev_desks)
    j += 1

def find_by_id(arr, _id):
    a = None
    for i in range(len(arr)):
        if _id == arr[i]._id:
            a = arr[i]
    
    return a

for i in range(len(dev_desks)):
    if len(developers)> 0:
        d = find_and_place_dev(dev_desks[0])
        dev_desks.pop(0)

for j in range(len(man_desks)):
    if len(pro_managers) > 0:
        pm = find_and_place_man(man_desks[0])
        man_desks.pop(0)

# print(man_desks_conf, dev_desks_conf)

for i in range(len(all_developers)):
    d = find_by_id(dev_desks_conf, all_developers[i]._id)
    if d:
        print(" ".join(map(str, d.desk)))
    else:
        print("X")

for i in range(len(all_managers)):
    pm = find_by_id(man_desks_conf, all_managers[i]._id)
    if pm:
        print(" ".join(map(str, pm.desk)))
    else:
        print("X")

