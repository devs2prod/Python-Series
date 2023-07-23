def BinarySearch(li, key):
    low = 0 
    high = len(li) - 1
    mid = 0

    while(low <= high):
        mid = (high + low) // 2

        if(li[mid] < key):
            low = mid + 1

        elif(li[mid] > key):
            high = mid - 1

        else:
            return mid

    return -1

li = []
n = int(input("Enter the number of elements: "))
for i in range(1, n+1):
    ele = int(input("Enter element: "))
    li.append(ele)

key = int(input("Enter the element to be searched: "))

result = BinarySearch(li, key)

if(result != -1):
    print("Element is present at index", str(result))
else:
    print("Element is not presnet in the array")