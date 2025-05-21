def outer_function():
    var1 = 40
    print(var1)

    def inner_function1():
        var2 = 60
        print(var2)

    def inner_function2():
        print(var1)

    #  print(var2) --> Not possible
    inner_function1()
    inner_function2()


#  print(var2)  --> not possible
outer_function()
