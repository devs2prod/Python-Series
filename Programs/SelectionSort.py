def SelectionSort(li, n):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if(li[min] > li[j]):
                min = j
        li[i], li[min] = li[min], li[i]

    return li
    
li = []
n = int(input("Enter the number of elements to be sorted: "))
for i in range(1, n+1):
    ele = int(input("Enter the element: "))
    li.append(ele)

print("List before sorting: ", li)
print("List after sorting: ", SelectionSort(li, n))
