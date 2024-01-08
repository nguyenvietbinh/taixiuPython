n =  int(input())
a = input()
lst = a.split(' ')
# 1 3 2 4 1 2
def demSoNguoiNhinThay(arr):
    d = len(arr)
    lastIndex = arr[len(arr)-1]
    a = 0
    for i in range(d-1):
        if arr[i] >= lastIndex:
            a = i
    newArray = arr[a:]
    return len(newArray) - 1
for i in range(n):
    if i == 0:
        print(0)
    else:
        
        print(demSoNguoiNhinThay(lst[0:i+1]))
