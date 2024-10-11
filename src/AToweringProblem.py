#https://open.kattis.com/problems/towering

from itertools import combinations

data = list(map(int,input().split()))
boxHeights = sorted(data[0:6])
v = data[6:8]
answers = []
ans = ""
combinaciones = list(combinations(boxHeights,3))
for i in range(len(v)):
    for comb in combinaciones:
        if sum(comb) == v[i]:
            answers.append(sorted(comb,reverse=True))

for i in range (len(answers)):
    for j in range (len(answers[i])):
        ans += f"{answers[i][j]} "

print(ans)