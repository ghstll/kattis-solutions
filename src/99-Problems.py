#https://open.kattis.com/problems/99problems
n = int(input())

beforeN = None
afterN = None
i = n
j = n

if n <= 99:
    beforeN = 99
    print(beforeN)
else:
    while i >=0:
        if str(i).endswith('99'):
            beforeN = i
            break
        else:
            i-=1
    while True:
        if str(j).endswith('99'):
            afterN = j
            break
        else:
            j+=1
    if abs(beforeN - n) < abs(afterN-n):
        print(beforeN)
    elif abs(afterN-n) < abs(beforeN-n):
        print(afterN)
    else:
        print(afterN)