def LinearSearch(li, n,key):
    flag = 0
    count = 0
    for i in range(n):
        if(key == i):
            flag = 1
            break
        count += 1
    return flag

li = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    ele = int(input("Enter element: "))
    li.append(ele)

key = int(input("Enter the element to find: "))
if(LinearSearch(li, n, key)):
    print("Element found")
else:
    print("Element not found")
