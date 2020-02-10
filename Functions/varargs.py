def printme(arg,*names):

    print("type of passed argument is ",type(names))
    print(arg)
    for n in names:
        print(n)

printme("aaa")
printme("john", "David", "smith", "nick")



