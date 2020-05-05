# Assigment:
# Functions Intermediate II
#
# Objectives:
# Practice write functions and looping over dictionaries
# Better understanding how to traverse a list of dictionaries or through
# a dictionary of lists.
#

# Clear the screen
import os
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
# Update values in Dictionary and Lists
# ----------------------------------------------------------------------------------

# (1) Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]]
print('\n-----------------------------------------------------------------------------------')
print("**** Change the value 10 in x to 15. ****")
print('-----------------------------------------------------------------------------------\n')
print("x=", x)
print("x[1][0]=", x[1][0])
print("\nChange 10 in x to 15")
x[1][0] = 15
print("x=", x)

# (2) Change the last_name of the first student from 'Jordan' to 'Bryant'
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

# (3) In the sports_directory, change 'Messi' to 'Andres'.
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
