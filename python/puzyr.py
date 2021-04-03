arr = list(map(int,input().split()))
n = len(arr)
count = 0
for k in range (n-1):
    for i in range (n-1):
        print (f"comparing {arr[i]} and {arr[i+1]}")
        if arr[i] > arr[i+1]:
            count +=1
            arr[i], arr[i+1] = arr[i+1], arr[i]
print (arr)
print (count)
