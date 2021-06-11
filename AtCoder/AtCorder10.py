N = int(input())
n = []

time = 0
x = 0
y = 0
flag = 1
for i in range(N):
    n.append(list(map(int,input().split())))


for i in range(len(n)):
    x = abs(x - n[i][1])
    y = abs(y - n[i][2])
    time = n[i][0] - time
    if((x + y) > time):
        flag = 0
    elif((time%2) != ((x + y)%2)):
        flag = 0

    

if(flag == 1):
    print('Yes')
else:
    print('No')