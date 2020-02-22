files = ["input_1.txt", "input_2.txt", "input_3.txt", "input_4.txt"]

f = open(f"inputs/{files[0]}")


START_X, START_Y, STOP_X, STOP_Y = map(int, f.readline().split())
N_OF_OBS = int(f.readline())

OBS = []

for i in range(N_OF_OBS):
    _ = map(int, f.readline().split())
    OBS.append(_)

f.close()