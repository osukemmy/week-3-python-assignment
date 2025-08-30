# Question 1: Large Power

## Problem
Create a function that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000.  

If the result is greater than 5000 → return **True**  
Otherwise → return **False**

---

## Function Definition
```python
def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
