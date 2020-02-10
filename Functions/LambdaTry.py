#Using Lambda inside another function
# def msg():
#     print("helo")
#     num=lambda a:a*a
#     a=int(input('enter a number:'))
#     print("SQuare is:",num(a))
#
# msg()

def function1():
    print("hello outer function")
    def function2():
        print("hello inner  function")
        function1()

    function2()





