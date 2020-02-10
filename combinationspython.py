def f(N:int , c:list):
    # solusion matrix
    s = []

    for index in range(len(c)):
        if index == 0 :
            s.append([list(c)])
        else :
            cost1 = min(s[1],s[2])
            cost2 = min(s[0],)



N = int(input())
c=[]
for i in range(N):
    c.append(map(int, input().split(' ')))

out_ = f(N,c)
print(out_)