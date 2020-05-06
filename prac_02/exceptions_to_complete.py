finished = False
result = 0
while not finished:
    try:
        chocolates = int(input("Enter how many chocolate do you have: "))
        people = int(input("Enter how many people in your class: "))
        result = chocolates / people
        print(result)
        pass
    except ValueError:
        print("Please enter a valid integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
print("Valid result is: ", result)