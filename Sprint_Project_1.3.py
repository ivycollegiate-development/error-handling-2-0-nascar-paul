try:
    age=int(input("Please enter your age: "))
except ValueError:
    print("This is not a valid response")

print("In one year, you will be ", age + 1)