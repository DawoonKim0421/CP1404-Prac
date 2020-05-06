"""
a. count in 10s from 0 to 100
"""
number_a = 0
while number_a < 101:
    print(number_a)
    number_a = number_a + 10

"""
b. count down from 20 to 1
"""
number_b = 20
while number_b > 0:
    print(number_b)
    number_b -= 1

"""
c. print n stars. Ask the user for a number, then print that many stars (*), all on one line
Note: this is a very simple loop for repeating n times. We use for loops for "definite"
 iteration like this. while loops are used for "indefinite" iteration (like repeating
 while a user input is incorrect).
"""
print("How many stars would you like to print?");
num_rows = int(input('Please enter the number of rows: '));
for row in range(0, num_rows):
    print("*", end=" ")
    print()

"""
d. print n lines of increasing stars. Using the same number as above print lines of increasing stars,
 starting at 1. E.g. if 4 was the number entered, your single loop should print
"""
def pypart(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
n = 4
pypart(n)