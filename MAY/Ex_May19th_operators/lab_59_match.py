# Match Statement -> # Switch in Java
# match the op and execute
# Python > 3.10
from re import match

# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block


# Write a program to ask the user which browser he want to run automation.
browser_name= input("Enter the Browser name:\n")
match browser_name :
    case "firefox":
        print("Starting Firefox !")
    case "Chrome":
        print("Chrome is starting!")
    case "Edge":
        print("Edge is starting!")
    case"Safari":
        print("Safari is starting!")
    case _:
        print("None of the browser! is Starting")
