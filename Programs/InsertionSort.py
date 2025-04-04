def InsertionSort(li, n):
    for i in range(1, n):
        temp = li[i]
        j = i - 1
        while((j >= 0) and (temp < li[j])):
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp

    return li

li = []
n = int(input("Enter the number of elements to be sorted: "))
for i in range(1, n+1):
    ele = int(input("Enter the element: "))
    li.append(ele)

print("List before sorting: ", li)
print("List after sorting: ", InsertionSort(li, n))
