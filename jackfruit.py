list1=list(map(int,input().split()))
n=list1[0]
d=list1[1]
total=0
list2=list(map(int,input().split()))
list2.sort()
for i in range(d):
    total+=list2[n-1]
    n-=1
print(total)
