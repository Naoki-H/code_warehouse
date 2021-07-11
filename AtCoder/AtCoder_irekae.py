N = int(input())

card = ['1','2','3','4','5','6']
tmp1 = 0
mod = 0

N = N % 30

for i in range(N):
    mod = i % 5
    card[mod],card[mod+1] = card[mod+1] , card[mod]


print(''.join(card))