#https://open.kattis.com/problems/3dprinter


n = int(input())
day = 1
statuesMade = 1
while statuesMade < n:
    day += 1
    statuesMade *= 2
print(day)

