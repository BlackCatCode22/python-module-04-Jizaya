filename = input("Enter a file name: ")
try:
    with open(filename) as file:
        for line in file:
            print(line.upper().rstrip())
