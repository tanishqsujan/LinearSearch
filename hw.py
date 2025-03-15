def search(arr, x,n):
    last= -1
    for i in range(0,n):
        if (arr[i]== x):
            last= i
        
    return last

arr= [44,44,60,70,69,33,44]
x= 44
n= len(arr)

result= search(arr,x,n)

if (result== -1):
    print("Element not found")
else:
    print("Element found at index",result)