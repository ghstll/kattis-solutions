numbers = sorted(list(map(int,input().split())))
order = input().upper()
dicc = {}
c = 'A'
ans = ""
for i in range(len(numbers)):
    dicc[c] = numbers[i]
    c = chr(ord(c)+1)
    
for i in range(len(order)):
    ans += str(dicc[order[i]]) + " "
print(ans)

