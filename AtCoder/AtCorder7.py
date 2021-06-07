import sys

num ,yen= map(int, input().split())
sen = 1000
gosen = 5000
man = 10000

sen_num = -1
gosen_num = -1
man_num = -1

for ii in range(int(yen/gosen)+1):
    for iii in range(int(yen/man)+1):
        if((ii - (yen/1000-num-9*iii)/4 == 0) and (ii + iii) <= num ):
            man_num = iii
            gosen_num = ii
            if((num - gosen_num - man_num) < 0 ):
                break
            else:
                print(man_num,gosen_num,(num - gosen_num - man_num))
                sys.exit()

print(-1,-1,-1)