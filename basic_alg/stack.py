#coding=utf-8

from typing import List

class Stack:
    aList = []
    len=0

    def __init__(self, list):
        self.aList = list
        self.len = len(self.aList)

    def isEmpty(self):
        if self.len ==0:
            return True
        else:
            return False

    def push(self, object):
        self.aList.append(object)
        self.len +=1

    def pop(self):
        if (self.isEmpty()):
            print("Empty stack, can't pop object.")
            return None
        else:
            object = self.aList[-1]
            self.aList = self.aList[:self.len-1]
            self.len -= 1
            return object

    def top(self):
        if (self.isEmpty()):
            print("Empty stack, can't pop object.")
            return None
        else:
            return self.aList[-1]

    def size(self):
        return self.len

    def printStack(self):
        if self.isEmpty():
            print("The stack is empty.")
        else:
            for i in range(self.len-1,-1,-1):
                print(self.aList[i])

if __name__ == '__main__':
    stack = Stack([])
    stack.push("Reid")
    stack.push("Elsa")
    print(stack.size())
    print(stack.top())
    print(stack.size())
    print(stack.pop())
    print(stack.size())
    print(stack.pop())
    print(stack.size())
    print(stack.pop())
    print(stack.size())
    stack.printStack()