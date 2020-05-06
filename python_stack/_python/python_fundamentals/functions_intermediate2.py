# Assigment:
# Functions Intermediate II
#
# Objectives:
# Practice write functions and looping over dictionaries
# Better understanding how to traverse a list of dictionaries or through
# a dictionary of lists.
#

import os

# Clear the screen
os.system('clear')


x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first-name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'curry'], 'soccer': ['Messi', 'Ronaldo', 'Roomy']
}
z = [{'x': 10, 'y': 20}]

# ----------------------------------------------------------------------------------
# (1) Update values in Dictionary and Lists
# ----------------------------------------------------------------------------------

# (1-1) Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]]
print('\n-----------------------------------------------------------------------------------')
print("**** Change the value 10 in x to 15. ****")
print('-----------------------------------------------------------------------------------\n')
print("x=", x)
print("x[1][0]=", x[1][0])
print("\nChange 10 in x to 15")
x[1][0] = 15
print("x=", x)

# (1-2) Change the last_name of the first student from 'Jordan' to 'Bryant'
print('\n-----------------------------------------------------------------------------------')
print("**** Changing the last_name of the first student from 'Jordan' to 'Bryant' ****")
print('-----------------------------------------------------------------------------------\n')
print('students=', students)
print('\nShow the FIRST student info')
print('students[0]["last_name"]', students[0]['last_name'])
print('\nCHANGE the last_name of the first student from Jordan to Bryant')
students[0]['last_name'] = 'Bryant'
print('\nShow all students, including Michael BRYANT')
print('students=', students)

# (1-3) In the sports_directory, change 'Messi' to 'Andres'.
print('\n-----------------------------------------------------------------------------------')
print("**** Change 'Messi' to 'Andres' in the sports_directory ****")
print('-----------------------------------------------------------------------------------\n')
print('Show the entire sports directory')
print('sports_directory', sports_directory)
print('\nShow the soccer info')
print('sports_directory["soccer"]', sports_directory['soccer'])
print('\nShow "Messi')
print('sports_directory["soccer"][0]', sports_directory['soccer'][0])
print('\nChange the name of Messi to Andres')
sports_directory['soccer'][0] = 'Andres'
print('\nShow modified sports directory')
print('sports_directory', sports_directory)

# (1-4) Change the value 20 in z to 30
print('\n-----------------------------------------------------------------------------------')
print("**** Change the value 20 in z to 30 ****")
print('-----------------------------------------------------------------------------------\n')
print("z", z)
print("\nChange the value of y to 30")
z[0]['y'] = 30
print("z", z)
print()

# ----------------------------------------------------------------------------------
# (2) Iterate through a list of dictionaries
# ----------------------------------------------------------------------------------

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for x in some_list:
        print("first_name - {}, last_name - {}".format(x.get('first_name'),
                                                       x.get('last_name')))


print('\n----------------------------------------------------------------------------------')
print('Iterate through the list of students. First Version (hardcode key names)')
print('----------------------------------------------------------------------------------\n')
iterateDictionary(students)


# ----------------------------------------------------------------------------------
# (2a) Iterate through a list of dictionaries.  Use ternary operator for print
#
# I created this second iterateDictionary() function to use key name instead of
# hardcoding 'first_name' and 'last_name' in the print statement
# (see how I did it above).
#
# I didn't like hardcoding, but notice that we want a comma after the first_name
# key and value, but NOT after the last_name key and value. So below I print a
# different line (with and without comma), depending on value of the key (y).
#
# This uses the python ternary operator, which is weirder than in js or other
# languages.
#
# From this site:
# https://www.tutorialspoint.com/ternary-operator-in-python
#
# Sample of ternary operator
#  print("x" if x> y else "y")
# ----------------------------------------------------------------------------------

def iterateDictionary_a(some_list):
    for x in some_list:
        for y in x:
            print("{} - {}, ".format(y, x.get(y)), end='') if y == 'first_name' else print(
                "{} - {} ".format(y, x.get(y)), end='')
        print()
    # print()


print('\n----------------------------------------------------------------------------------')
print('Iterate through the list of students. Second version (dynamic key names)')
print('----------------------------------------------------------------------------------\n')
iterateDictionary_a(students)

# ----------------------------------------------------------------------------------
# (3) Get values from a list of dictionaries
# ----------------------------------------------------------------------------------


def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])


print('\n----------------------------------------------------------------------------------')
print('Get values from a list of dictionaries')
print('----------------------------------------------------------------------------------\n')

print('*** first_name key ***\n')
iterateDictionary2('first_name', students)

print('*** last_name key ***\n')
iterateDictionary2('last_name', students)

# ----------------------------------------------------------------------------------
# (4) Iterate through a dictionary with list values.
# ----------------------------------------------------------------------------------

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):

    for x in some_dict:  # Loop through dictionary items (there are two)

        # Print the number of array elements (locations or instructors) for this dictionary key
        print('\n' + str(len(some_dict[x])) + ' ' + x.upper())

        for y in some_dict[x]:  # loop through all the array elements
            print(y)

    print("\n**** DONE ****\n")


print('\n----------------------------------------------------------------------------------')
print('Iterate through a dictionary with list values')
print('----------------------------------------------------------------------------------\n')


printInfo(dojo)
