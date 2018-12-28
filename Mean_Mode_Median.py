n=int(input())
x=0
a = tuple(map(int,input().split()))
for i in range(n):
    x = x + a[i]
mean = x/n
print(mean)
#mode
a= sorted(a)
if(n%2==0):
    mode = a[int(n/2)]+a[int((n/2)-1)]
else:
    mode = a[n/2]
mode = mode/2    
print(mode)
#median
r=0
l=0
for i in range(n):
    y=a.count(a[i])
    if(y>l):
        l=y
    else:
        l=l
a = sorted(a,reverse = True)
for i in range(n):
    if(a.count(a[i])==l):
        r=a[i]
print(r)        
