class queue:
    def __init__(self):
        self.n=int(input("Enter the length of the queue:"))
        print("Enter the elements that already exist in the queue:")
        self.a=list(map(int,input().split()))
    def enqueue(self,data):
        if self.isfull():
            return None
        self.a.insert(0,data)
    def dequeue(self):
        if self.isempty():
            return None
        print("The element ",self.a.pop()," is deleted")
    def peek(self):
        if self.isempty():
            return None
        print(self.a[len(self.a)-1])
    def isfull(self):
        if self.n==len(self.a):
            print("The queue is full")
            return True
        return False
    def isempty(self):
        if len(self.a)==0:
            print("The queue is empty")
            return True
        return False
    def display(self):
        if self.isempty():
            return None
        elif self.isfull():
            return None
        print(*self.a)
    
a=queue()
while True:
    c=int(input("Options:1.enqueue,2.dequeue,3.peek,4.Display,5.exit:"))
    if c==1:
        a.enqueue(int(input("Enter the value u wish to enter in the queue:")))
        print()
    elif c==2:
        a.dequeue()
    elif c==3:
        a.peek()
    elif c==4:
        a.display()
    elif c==5:
        print("Program aborted")
        break
    else:
        print("Invalid input plz try again")
