pb_global_b = 12
def my_function():
    pb_a = 30
    print(pb_a)
    print(pb_global_b)
# print(pb_a)   # it is not possible as it was a local variable to my_function
print(pb_global_b)
my_function()