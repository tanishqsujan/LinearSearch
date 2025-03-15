def search(arr, x, n):
    for i in range(0,n):
        if (arr[i]== x):
            return i
        
    return -1


arr= [10,20,30,40,50,60]
x= 30
n= len(arr)

result= search(arr, x, n)

if (result== -1):
    print("Element not found")
else:
    print("Element found at index", result)