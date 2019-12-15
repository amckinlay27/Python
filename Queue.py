class Queue:
    def __init__(self):
        self.__contents = []

    def enqueue(self, item):
        self.__contents.append(item) #insert item at end

    def dequeue(self):
        tmp = self.__contents[0]
        del self.__contents[0] #remove from end
        return tmp

    def peek(self):
        return self.__contents[0]

    def empty(self):
        return len(self.__contents) == 0

    def length(self):
        return len(self.__contents)

    def __str__(self):
        return str(self.__contents)

def main():
    q1 = Queue()
    q1.enqueue(10)
    print(q1)
    q1.enqueue(20)
    print(q1)

    print("******")
    while(not q1.empty()):
        print(q1)
        q1.dequeue()

def stringTest():
    q1 = Queue()
    expression = "Adam"
    expression2 = ""

    print(expression)
    
    for c in expression:
        q1.enqueue(c)

    while(not q1.empty()):
        expression2 += q1.dequeue()

    print(expression2)

main()
