n = int(input())
main_array = tuple(map(int,input().split()))
weight_main_array = tuple(map(int,input().split()))
w_mean=0
x=0
for i in range(n):
    w_mean = w_mean + (main_array[i] *weight_main_array[i])
    x = x+ weight_main_array[i]
w_mean = w_mean/x
#use round to print up to 1 decimal
print(round(w_mean,1))
