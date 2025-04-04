def MergeSort(li):
    if len(li) > 1:

        right = len(li)//2
        left = li[:right]
        mid = li[right:]

        MergeSort(left)
        MergeSort(mid)

        i = j = k = 0

        while i < len(left) and j < len(mid):
            if left[i] < mid[j]:
                li[k] = left[i]
                i += 1
            else:
                li[k] = mid[j]
                j += 1
            k += 1

        while i < len(left):
            li[k] = left[i]
            i += 1
            k += 1

        while j < len(mid):
            li[k] = mid[j]
            j += 1
            k += 1

li = []
n = int(input("Enter the number of elements to be sorted: "))
for i in range(1, n+1):
    ele = int(input("Enter the element: "))
    li.append(ele)

print("List after sorting: ", li)
MergeSort(li)
print("List after sorting: ", li)
