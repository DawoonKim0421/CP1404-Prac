"""
Broken program to determine score status
"""

def main():
    """main method, starting point of program"""
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif 90 < score <=100:
        print("Excellent")
    elif 50 <= score <= 90:
        print("Passable")
    else:
        print("Bad")


if __name__ == '__main__':
    main()