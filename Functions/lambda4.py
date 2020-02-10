square=lambda x1:x1*x1

print("Square is:",square(10))


def test():
    print ("test")


def invoker(func):
        func()

invoker(test)  # prints test was invoked

