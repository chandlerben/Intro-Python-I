# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def is_even(a):
    if a % 2 == 0:
        print("Even!")
    else:
        print("Odd")


is_even(num)


def shorthand_if(a):
    print("This is shorthand even") if a % 2 == 0 else print("Shorthand odd!")


shorthand_if(num)
