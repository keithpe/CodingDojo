# Multiple Arguments

## Objectives:

- Create functions that can accept a varying number of arguments
- Recognize the splat operator

What if we want to pass in a varying number of arguments, or want to capture multiple arguments into a single parameter? Placing an asterisk before the name of the parameter after the "normal" parameters does just that. The asterisk is called a splat operator.

'''
def varargs(arg1, \*args):
print("Got ", arg1, " and ", args)
varargs("one") # output: Got one and ()
varargs("one", "two") # output: Got one and ('two',)
varargs("one", "two", "three") # output: Got one and ('two', 'three')
'''

In this example, the first argument arg1 is assigned to the first method parameter as usual. Notice, however, that any and all remaining arguments passed in are in the args parameter, which appears to be a tuple (as indicated by the () syntax)! Because we prefixed the final parameter with an asterisk (the splat operator), all the arguments that don't match a required parameter are packed into a single tuple.

Remember that a tuple is an iterable, just like a list. That means if we want to access each of the arguments passed over individually, we can use a loop:

'''
def varargs(arg1, \*args):
for a in args:
print(a)
varargs("one", "two", "three") # output: two, three (on separate lines)
'''
