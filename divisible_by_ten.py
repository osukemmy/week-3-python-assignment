def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


# Test cases
print(divisible_by_ten(20))   # True (20 is divisible by 10)
print(divisible_by_ten(25))   # False (25 is not divisible by 10)
print(divisible_by_ten(100))  # True (100 is divisible by 10)
print(divisible_by_ten(7))    # False (7 is not divisible by 10)
