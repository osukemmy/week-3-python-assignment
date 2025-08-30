# Question 2: Divisible by Ten

## Problem
Create a function that determines whether or not a number is divisible by ten.  
A number is divisible by ten if the remainder of the number divided by 10 is 0.  

---

## Function Definition
```python
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
