def type_check(typ):
    def decorator(fn):
        def wrapper(*args):
            if not isinstance(*args, typ):
                return "Bad Type"
            result = fn(*args)
            return result
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))