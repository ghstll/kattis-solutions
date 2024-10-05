def problem():
    answers = []
    P = int(input())
    for _ in range(P):
        data = list(map(int,input().split()))
        answers.append(f"{data[0]} {result(data[1])}")
    for answer in answers:
        print(answer)


def result(n):
    route = []
    while n != 1:
        route.append("R" if n%2 else "L")
        n //= 2
    p,q = 1,1
    for step in route[::-1]:
        if step == "L":
            q = p + q
        else:
            p = p + q
    return f"{p}/{q}"

problem()