class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for num2 in nums:
            self.result += num2
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for num2 in nums:
            self.result -= num2
        return self


md = MathDojo()
# to test:

x = md.add(1).add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).add(
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1).add(5).result
print(x)
# This sets the result attribute to zero, so it doesn't affect our next call.
md.result = 0

x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
md.result = 0  # Set result back to zero, so it doesn't interfere with the next call

# run each of the methods a few more times and check the result!
y = md.add(3).add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).subtract(
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1).result
print(y)
md.result = 0

# This also set result back to zero
md.__init__()
print(md.result)
