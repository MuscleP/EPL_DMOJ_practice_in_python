'''
init() initialize an empty stack and return None.
push(val) push an integer element val into the top of stack and return None
pop() removes the element at the top of the stack and return None.
top() return the top element of the stack.
getSquareSum() calculate the square sum of all elements in the stack, you should return 0 if the stack is empty.
'''

def init():
    stack.clear()
    global square_sum
    square_sum = 0
def push(val):
    global square_sum
    square_sum += val ** 2
    stack.append(val)
def pop():
    global square_sum
    square_sum -= top() ** 2
    stack.pop()
def top():
    return stack[-1]
def getSquareSum():
    return square_sum

stack = []
square_sum = 0