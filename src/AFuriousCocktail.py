#https://open.kattis.com/problems/cocktail

N , T = map(int,input().split())
e = []
for i in range(N):
    e.append(int(input()))
effects = sorted(e,reverse=True)
for i in range(len(effects)):
    effects[i]  = effects[i] - ((len(effects)-i-1)*T)
if 0 in effects: 
    print("NO")
else:
    print("YES")

