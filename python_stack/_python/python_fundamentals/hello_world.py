# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name)  # with a comma
print("Hello " + name)  # with a +

# 2a
myName = "Keith Peterson"
print("Hello", myName)

# 2b
print("Hello " + myName)

# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)  # with a comma
# print("Hello " + name)  # with a +	-- this one should give us an error!

num = 73
# 3a Print "Hello {{num}}!" using a comman in the print function
print("Hello", num)
# 3b Print the string "Hello {{num}}!", using a + in the print function.
# Convert num, which is integer into a string before using + to concatenate.
print("Hello " + str(num))


# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(
    fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}")  # with an f string
