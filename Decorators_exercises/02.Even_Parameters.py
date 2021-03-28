def even_parameters(fn):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, int) or i % 2 != 0:
                return f"Please use only even numbers!"
        result = fn(*args, **kwargs)
        return result
    return wrapper




@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))