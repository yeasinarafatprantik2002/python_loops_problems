n_num = int(input("Enter the value of n: "))
n_num_sum = 0

for i in range(1, n_num + 1):

    if i % 2 == 0:
        n_num_sum += i
print("Sum of even numbers is: ", n_num_sum)
