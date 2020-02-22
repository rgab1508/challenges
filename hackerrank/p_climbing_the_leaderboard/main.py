
f = open("a.in")

NO_OF_PLAYERS = int(f.readline())
L_SCORES = [int(c) for c in f.readline().split(" ")]
NO_OF_GAMES_PLAYED = int(f.readline())
SCORES = [int(c) for c in f.readline().split(" ")]
OUTPUT = []

scoreboard = list()


def rank_scores(_scores):
    _scores = set(_scores)
    _scores = list(_scores)

    _scores = sorted(_scores, reverse=True)

    for i in range(len(_scores)):
       scoreboard.append((_scores[i], i+1))


def get_rank_from_sb(sb, item):
    for i in range(len(sb)):
        if item == sb[i][0]:
            return sb[i][1]
    

for i in SCORES: 
    L_SCORES.append(i)
    rank_scores(L_SCORES)
    OUTPUT.append(get_rank_from_sb(scoreboard, i))
# L_SCORES.extend(SCORES)

def in_score_board(sb, item):
    for i in range(len(sb)):
        if item == sb[i][0]:
            return True, sb[i]
    
    return False, None


# for i in SCORES:
#     in_sb, rank = in_score_board(scoreboard, i)
#     if in_sb:
#         OUTPUT.append(rank)


print(SCORES)
print(L_SCORES)
print(scoreboard)
print(OUTPUT)

