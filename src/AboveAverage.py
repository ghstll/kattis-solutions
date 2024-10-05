#https://open.kattis.com/problems/aboveaverage

c = int(input())
for i in range(c):
    listGrades = list(map(int,input().split()))
    prom = sum(listGrades[1:])/(len(listGrades)-1)
    n = 0
    for grade in listGrades[1:]:
        if grade > prom:
            n += 1
    percent = round((n/(listGrades[0])) * 100,3)
    print(f"{percent:.3f}%")
            

    
        
    