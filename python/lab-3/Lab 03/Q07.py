def stack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def length(stack):
    return len(stack)


def push(stack, item):
    stack.append(item)
    print("pushed item:", item)


def pop(stack):
    if (isEmpty(stack)):
        return "stack is empty"
    return stack.pop()


def reverse(string):
    n = len(string)
    s = stack()
    for i in range(0, n, 1):
        push(s, string[i])
    string = ""
    for i in range(0, n, 1):
        string += pop(s)
    return string


string = "RonJacob"
string = reverse(string)
print("Reversed string is " + string)
