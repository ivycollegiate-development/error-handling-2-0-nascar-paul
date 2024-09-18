try:
    # This is the code that may generate a failure in the program
    age=int(input("Please enter your age: ")) # This is also considered a comment
    # Below is another way to comment out code
    """
    Anything in this space will not be EXECUTED
    """
except NameError:
    print("This is not a valid response")
    break  # Exit the program if the response is not valid
print (f"Your age is ", {age}) # This prints out the return value to the console
# print("In one year, you will be ", age + 1)