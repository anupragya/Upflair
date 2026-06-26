#print prime no. from a list
numbers = [10, 7, 13, 20, 29, 35, 17]

print("Prime numbers are:")

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)