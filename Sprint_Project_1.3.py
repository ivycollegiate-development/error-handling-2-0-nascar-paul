try:
    # This is the code that may generate a failure in the program
    age=int(input("Please enter your age: ")) # This is also considered a comment
    # Below is another way to comment out code
    """
    Anything in this space will not be EXECUTED
    """
except ValueError:
    print("This is not a valid response")
# There is no point in telling someone why something has already failed
# print("In one year, you will be ", age + 1)