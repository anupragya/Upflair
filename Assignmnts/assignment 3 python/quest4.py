#function to count simple interest
def simple_interest(principal, rate=5, time=1):
    si = (principal * rate * time) / 100
    return si


# Positional Arguments
print("Simple Interest =", simple_interest(10000))

# Keyword Arguments
print("Simple Interest =", simple_interest(principal=10000, rate=8, time=2))