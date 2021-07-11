A ,B ,X = map(int, input().split())

min , max =0 , 10**9+1
median = 0

while(min + 1 != max):
    median = int((min+max)/2)
    if( (A*median + B*len(str(median))) <= X ):
        min = median
    else: 
        max = median
print(min)
        
        




