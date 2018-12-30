import math
input1 = int(input())
values = tuple(map(int,input().split()))
len1 = len(values)
sum1 = 0
mean = sum(values)/len1
for i in range(len1):
    sum1 = sum1 + ((mean - values[i])**2)
final = math.sqrt(sum1/len1)
print(round(final,1))
