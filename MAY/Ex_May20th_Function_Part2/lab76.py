public_toilet = "PB"

def home():
    private_toilet = "PT"
    print(public_toilet)
# print(private_toilet) which is not possible as it was a local to home() function,
# we can't access private variables locally
def stranger():
    print(public_toilet)
    # print(private-toilet) which is not possible as it was a local to home()

# print(private_toilet) which is not possible as it was a local to home()
print(public_toilet)
home()
stranger()