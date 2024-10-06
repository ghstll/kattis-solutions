#https://open.kattis.com/problems/rankproblem
n , m = map(int, input().split())
ranking = []
for i in range(1,n+1):
    ranking.append(f"T{i}")

for i in range(m):
    w , l = input().split()
    if ranking.index(w) > ranking.index(l):
        team = ranking.pop(ranking.index(l))       
        ranking.insert(ranking.index(w)+1,team) 


for team in ranking:
    print(team + " ")

