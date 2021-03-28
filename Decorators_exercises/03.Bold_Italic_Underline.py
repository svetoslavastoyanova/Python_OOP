def make_bold(fn):
    def decorator(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"<b>{result}</b>"
    return decorator


def make_italic(fn):
    def decorator(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"<i>{result}</i>"
    return decorator


def make_underline(fn):
    def decorator(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f"<u>{result}</u>"
    return decorator


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))