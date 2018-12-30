def check(y,start,end):
    y = y[start:end]
    l=int(len(y))
 #   print(y)
  #  print(l)
    a=int(l/2)
   # print(a)
    b = int(a-1)
    if(l%2 == 0):
        print(int((y[b]+y[a])/2))
    else:
        print(int((y[int(a)])))
    
x= int(input())
y = tuple(map(int, input().split()))
y = sorted(y)
l = int(len(y))
#print(y)
a=int(l/2)
            #a=4
b = int(a-1)
            #b=3
if(l%2 == 0):
    check(y,0,(a))
    print(int((y[b]+y[a])/2))
else:
    check(y,0,(a))
    print(int(y[int(a)]))

#print(y)
if(l%2 == 0):
    check(y,a,l)
    
else:
    check(y,(a+1),l)

