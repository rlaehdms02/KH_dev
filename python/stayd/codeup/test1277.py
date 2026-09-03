a = int(input())
num_a = list(map(int,input().split()))[:a]
for i in range(a+2):
    if a == 1:
        print(num_a[i] , end=" ")
        print(num_a[i], end=" ")
        print(num_a[i], end=" ")
        break
    elif i == 0:
        print(num_a[i] , end=" ")
    elif i == a-1:
        print(num_a[i] ,end=" ")
    elif (a//2) == (i):
        print(num_a[i] ,end=" ")
    else:
        continue
