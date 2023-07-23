def Expo(x, n):
    res = 1
    for i in range(1, n+1):
        res *= x
    return res

x = int(input("Enter the value of the number: "))
n = int(input("Enter the power of the number: ")) 
print("Value to be calculated: ", x, "^", n)
print("Actual result: ", x ** n)
print("Calculated result: ", Expo(x, n))
