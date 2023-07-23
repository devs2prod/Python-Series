def FindMax(li):
    max = li[0]
    for i in li:
        if i > max :
            max = i
    return max

li = []
n = int(input("Enter the number of elements in the list: "))
for i in range(1, n + 1):
    ele = int(input("Enter element: "))
    li.append(ele)

print("Largest element is: ", FindMax(li))
