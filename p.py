n = int(input())
l = int(input())
r = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

for i in range(l,-1):
    print(arr[i], end=' ')