num = int(input("Enter the value of n: "))
is_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print(num, "is prime: ", is_prime)
