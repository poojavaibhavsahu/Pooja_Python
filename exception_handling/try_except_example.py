try:
    a=10/0
    print(a)
except ZeroDivisionError:
    print("this statent is raisingan exception")

else:
 print   ("stament executed")
finally:
    print("all statmennt will execute")