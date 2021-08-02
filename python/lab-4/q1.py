class priorityqueue:
    def __init__(self):
        self.a=[]
    def add(self, pri,value):
        self.a.append([pri,value])
    def min(self):
        if self.is_empty():
            print("The queue is empty")
            return
        return min(self.a)
    def is_empty(self):
        if(self.a==[]):
            return True
        return False
    def remove_min(self):
        if self.is_empty():
            print("The array is now empty")
            return
        print("The value ",self.min()," has been removed")
        self.a.remove(min(self.a))
    def display(self):
        if self.is_empty():
            print("The queue is empty")
            return
        print(*self.a)

a=priorityqueue()
while(True):
    print("These are the following options:\n1-add an element\n2-checking the min priority element\n3-removing the element of highest priority\n4-Displaying the priority queue\n5-exit program")
    c=int(input())
    if c==1:
        n=int(input("Enter the number of inputs to be added:"))
        while(n):
            pri=int(input("Enter the priority of the value:"))
            value=input("Enter the value:")
            a.add(pri,value)
            n-=1
    elif c==2:
        print("The value of highest priority:",a.min())
    elif c==3:
        a.remove_min()
    elif c==4:
        a.display()
    elif c==5:
        print("Program Terminated")
        break
        