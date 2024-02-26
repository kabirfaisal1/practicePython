# This program is used to demonstrate the syntax of variables in python.
'''A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''
print("Creating a variable in python is very easy. We just need to assign a value to it.");
print("In python, we use variable to store data. Variables are not executed by the interpreter.");
'''
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.'''
x = 14;
print("In python x=5 will be into integer because it as a integer value:", x);
y = "Kabir";
print("In python y= Kabir will be into string because it as a string value:", y);

print("Casting: If you want to specify the data type of a variable, this can be done with casting.");
a = str("14");
print("In python a=14 will be into string because it as a string value:", a);
b = int(14);
print("In python b=14 will be into integer because it as a integer value:", b);
c= float(14);
print("In python c=14 will be into float because it as a float value:", c);

## Single or Double Quotes
print("In python, we can use single or double quotes to represent a string.");
x = "Kabir";
print("In python x= Kabir with double quotes", x);
y = 'Kabir';
print("In python y= Kabir with single quotes", y);
