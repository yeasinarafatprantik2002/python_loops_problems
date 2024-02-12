num = int(input("Enter the value of n: "))
factorial = 1

# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial of", num, "is: ", factorial)

while num > 0:
    factorial *= num
    num -= 1
print("Factorial is: ", factorial)
