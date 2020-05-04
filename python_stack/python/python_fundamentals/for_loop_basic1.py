
print("------------------------------------------------------------")
print("Basic - print all integers from 0 to 150")
print("------------------------------------------------------------")

for i in range(0, 151, 1):
    print(i)

print("------------------------------------------------------------")
print("Multiples of 5 - Print all the multiples of 5 from 5 to 1000")
print("------------------------------------------------------------")

for i in range(5, 1005, 5):
    print(i)

print("----------------------------------------------------------------------------------------------------------------------------------")
print("Counting, the Dojo Way - print integers 1 to 100. If divisible by 5 print 'Coding' instead. If divisible by 10 print 'Coding Dojo'")
print("----------------------------------------------------------------------------------------------------------------------------------")

for i in range(1, 101, 1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

print("-----------------------------------------------------------------------------------------------------")
print("Whoa. That Sucker's Huge - Add odd integers from 0 to 500, 000 and print the final sum.")
print("-----------------------------------------------------------------------------------------------------")

odd = 0
for i in range(0, 500001, 1):
    if i % 2 != 0:
        odd += i
print("The sum of odd numbers is: {0:9d}".format(odd))

print("-----------------------------------------------------------------------------------------------------")
print("Countdown by fours - Print positive numbers starting at 2018, counting down by fours.")
print("-----------------------------------------------------------------------------------------------------")

for i in range(2018, 0, -4):
    print(i)

print("-----------------------------------------------------------------------------------------------------------------------")
print("Flexible counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print")
print("only the integers that are multiple of mult. For example, if lowNum=2, highNum=9 and mult=3, the loop should print 3,")
print("6,9 (on successive lines).")
print("-----------------------------------------------------------------------------------------------------------------------")

lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum+1, 1):
    if i % mult == 0:
        print(i)

print("------------")
print("Done")
print("------------")
