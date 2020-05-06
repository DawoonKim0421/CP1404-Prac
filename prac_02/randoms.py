import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
Q.  What did you see on line 1?
Q1. What was the smallest number you could have seen, what was the largest?
A1-1. Smallest: 5
A1-2. Largest: 20

Q.  What did you see on line 2?
Q1. What was the smallest number you could have seen, what was the largest?
Q2. Could line 2 have produced a 4?
A1-1. Smallest: 3
A1-2. Largest: 9
A2. No, it produces only {3, 5, 7, 9}

Q.  What did you see on line 3?
Q1. What was the smallest number you could have seen, what was the largest?
A1-1. Smallest: 2.5
A1-2. Largest: 5.5
"""