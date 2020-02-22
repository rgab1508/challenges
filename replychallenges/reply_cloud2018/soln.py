"""
    V -> no of Providers
    S -> no of Servies
    C -> no of Countries
    P -> no of Projects
    rv -> no of regions
"""

from base.base import Project, Provider, Region

files = ["first_adventure.in", "second_adventure.in", "third_adventure.in", "fourth_adventure.in"]
f = open(f"inputs/{files[0]}")
V, S, C, P = map(int, f.readline().split())
PROVIDERS = []
PROJECTS = []

S_names = f.readline().split()

C_names = f.readline().split()

for i in range(V):
    name, rv = f.readline().split(" ")
    rv = int(rv)
    regions = []
    for j in range(rv):
        r_name = f.readline()
        l = f.readline().split()
        nsup, csp, ui = l[0], l[1], l[2:]
        latency = f.readline().split()

        r = Region(r_name, nsup, csp, ui)
        regions.append(r)

    v = Provider(name, rv, regions)
    PROVIDERS.append(v)


    
for k in range(P):
    l = f.readline().split()
    base_penalty, target_country, amount_of_service = l[0], l[1], l[2:]
    p = Project(base_penalty, target_country, amount_of_service)
    PROJECTS.append(p)

