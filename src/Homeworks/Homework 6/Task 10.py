# Create a decorator that counts the number of times a function has been called.

dictt = {}


def decorator(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if fn.__name__ in dictt:
            dictt[fn.__name__] += 1
        else:
            dictt[fn.__name__] = 1
        return result

    return wrapper


@decorator
def esim1():
    return 1


@decorator
def esim2():
    return "Agnes"


@decorator
def esim3():
    pass


esim1()
esim1()
esim2()
esim2()
esim3()

print(dictt)
