def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False


# Test cases
print(large_power(2, 13))   # True (8192 > 5000)
print(large_power(2, 10))   # False (1024 < 5000)
print(large_power(10, 3))   # False (1000 < 5000)
print(large_power(20, 3))   # True (8000 > 5000)
