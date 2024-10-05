#https://open.kattis.com/problems/different
import sys
for line in sys.stdin:
    x,y = map(int,line.split())
    print(abs(x-y))
