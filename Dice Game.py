def count(arr, m, n):
    count = [0 for i in range(n + 1)]
    count[0] = 1
    for i in range(1, n + 1):
        for j in range(m):
            if (i >= arr[j]):
                count[i] += count[i - arr[j]]
    return count[n]


for i in range(int(input())):
    l=input().split()
    arr=[]
    for i in range(1,int(l[1])+1):
        arr.append(i)
    result=count(arr,int(l[1]),int(l[0]))
    print(result)
