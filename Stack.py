#Stack
class Stack:

    def __init__(self):
        self.__contents = []

    def __str__(self):
        return str(self.__contents)
    
    def push(self, item):
        self.__contents.insert(0, item)

    def pop(self):
        tmp = self.__contents[0]
        del self.__contents[0]
        return tmp

    def peek(self):
        return self.__contents[0]

    def length(self):
        return len(self.__contents)

    def empty(self):
        return len(self.__contents) == 0

    
def bracketMatching():
    expression = "[(3+2)*5]"
    stack1 = Stack()
    openingBrackets = ['[', '{', '(']
    closingBrackets = [']', '}', ')']

    for c in expression:
        if(c in openingBrackets):
            stack1.push(c)
        elif(c in closingBrackets):
            if(not stack1.empty()):
                top = stack1.pop()
                if(openingBrackets.index(top) != closingBrackets.index(c)):
                    print("Incorrect bracket types")
            else:
                print("There are more opening brackets than closing!")

def reverseString():
    expression = "adam McKinlay"
    stack1 = Stack()
    reverse = ""

    print(expression)
    
    for c in expression:
        stack1.push(c)

    while(not stack1.empty()):
        reverse += stack1.pop()

    print(reverse)
                
bracketMatching()
reverseString()
