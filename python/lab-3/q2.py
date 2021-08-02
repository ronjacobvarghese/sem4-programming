class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
        
        
class linked_list:
    
    
    def __init__(self):
        self.head=node()
        self.tail=node()
        
        
    def append(self,data):
        new_node=node(data)
        if self.head.next==None:
            self.head.next=new_node
        else:
            self.tail.next=new_node
        self.tail=new_node
        
        
        
    def len(self):
        l=0
        cur=self.head
        while cur.next!=None:
            l+=1
            cur=cur.next
        return l
    
    
    
    def display(self):
        cur=self.head
        
        if cur.next==None:
            print("The stack is currently empty")
            
        while cur.next!=None:
            cur=cur.next
            print(cur.data,end=" ")
        print()
        
        
        
    def insert(self, index,data):
        cur=self.head
        new_node=node(data)
        if(index>self.len()):
            print("Given index greater than the length of the linked_list\nHence node is appended")
            return self.append(data)
        if(index<0):
            print("Invalid index plz try again")
        if index==1:                
            new_node.next=cur.next
            cur.next=new_node
            return None
        cur_index=1
        while cur.next!=None:
            cur_index+=1
            cur=cur.next
            if cur_index==index:
                new_node.next=cur.next
                cur.next=new_node
                return None
            
    def deletion(self,index):
        cur=self.head
        if index>self.len() or index<0:
            print("deletion aborted out of range")
            return None
        if index==1:
            cur.next=cur.next.next
            return None
        cur_index=1  
        while cur.next!=None:
            cur=cur.next
            if cur_index+1==index:
                print("Element deleted:",cur.next.data)
                cur.next=(cur.next).next
                return None
            cur_index+=1
        
    def search(self,data):
        cur=self.head
        cur_index=1
        while cur.next!=None:
            cur=cur.next
            if cur.data==data:
                print("The integer was found in index",cur_index)
                return None
            cur_index+=1
        print("The integer was not found ")
            
                9567830466
class stack:
    def __init__(self):
        self.a=linked_list()
    
    def push(self,data):
        self.a.append(data)
    
    def pop(self):
        self.a.deletion(self.a.len())
    
    def top(self):
        if self.IsEmpty():
            return None
        print("The element at the top of the stack is:",self.a.tail.data)
    def IsEmpty(self):
        if self.a.len()==0:
            print("The given stack is empty")
            return True
        return False

a=stack()
while True:
    c=int(input("Options:1.push,2.pop,3.top,4.Exit program:"))
    if c==1:
        a.push(int(input("Enter an integer to be pushed into the stack:")))
        print()
    elif c==2:
        a.pop()
        print()
    elif c==3:
        a.top()
        print()
    elif c==4:
        print("Program terminated")
        print()
        break
    else:
        print("Invalid Input plz try again")
        print()
    
