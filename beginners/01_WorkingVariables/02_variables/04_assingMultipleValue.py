'''Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:'''
print("Many Values to Multiple Variables")
x, y, z = "Anakin", "Leia", "Luke"
print("In this Example X will be Anakin: ", x)
print("In this Example Y will be Leia: ", y)
print("In this Example Z will be Luke: ", z)

'''One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:'''
print("One Value to Multiple Variables")
x = y = z = "Anakin"
print("In this Example x will be Anakin: ", x);
print("In this Example y will be Anakin: ", y);
print("In this Example z will be Anakin: ", z);

'''Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.'''
print("Unpack a Collection")
starWar = ["Anakin", "Leia", "Luke"]
x, y, z = starWar
print("In this Example X will be Anakin: ", x)
print("In this Example Y will be Leia: ", y)
print("In this Example Z will be Luke: ", z)
