N = int(input())
n = []
for i in range(N):
    n.append(int(input()))

ka_sort = sorted(n,reverse=True)
kagamimoti = 1

for i in range(len(ka_sort) - 1):
    if(ka_sort[i] > ka_sort[i+1]):
        kagamimoti = kagamimoti + 1
    elif(ka_sort[i] == ka_sort[i+1]):
        continue
    else:
        break
print(kagamimoti)