while True:
    num = int(input("Enter vale b/w 1 to 10: "))
    if 1 <= num <= 10:
        print("You entered: ", num)
        break
    else:
        print("Invalid input. Please enter again.")
