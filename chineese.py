n=int(input())
daylist=list(map(int,input().split()))
niglist=list(map(int,input().split()))
must=int(input())
daylist.sort()
niglist.sort()
j=n-1
extra=0
for i in range(n):
    teach=daylist[i]+niglist[j]
    if teach>must:
        extra+=teach-must
    j-=1
        
print(extra*100)   
