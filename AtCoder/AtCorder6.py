N ,a ,b = map(int, input().split())
allsum = 0

for i in range(N+1):
    n = list(str(i))
    sum_list = list(map(int,n))
    sumsum = sum(sum_list)
    if int(a) <= sumsum <= int(b) :
        allsum += i
print(allsum)



    

