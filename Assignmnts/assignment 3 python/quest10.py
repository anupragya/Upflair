#read numbers from a file and calculate total and average
try:
    file = open("numbers.txt", "r")

    numbers = []

    for line in file:
        numbers.append(int(line.strip()))

    total = sum(numbers)
    average = total / len(numbers)

    print("Total =", total)
    print("Average =", average)

    file.close()

except FileNotFoundError:
    print("Error: File does not exist.") 