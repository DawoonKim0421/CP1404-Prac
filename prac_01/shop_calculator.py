"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that
 total before the amount is displayed on the screen.
"""
lst = []
num_item = int(input('Number of items: '))
for n in range(num_item):
    numbers = int(input('Price of item: '))
    lst.append(numbers)
print("Total price for", num_item, "items is", sum(lst))