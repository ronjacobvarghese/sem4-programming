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
            print("The linked list is currently empty")
            
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
            print("deletion aborted,index out of range")
            return None
        if index==1:
            cur.next=cur.next.next
            return None
        cur_index=1  
        while cur.next!=None:
            cur=cur.next
            if cur_index+1==index:
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
            
                
                
            
            
a=linked_list()
n=int(input("Enter the length:"))
for i in range(n):
    a.append(int(input("Enter a integer:")))
while(True):
    print("Select an option\n 1. Inserting elements \n 2. deleting elements  \n 3. displaying the elements \n 4. searching an element \n 5.exit the program\n")
    c=int(input())
    
    
    if(c==1):
        print("Do you wish to:\n 1. insert at the beginning \n 2. insert at the end \n 3. insert at some index\n")
        d=int(input())
        m=int(input("The value u wish to insert:"))
        if(d==1):
            a.insert(1,m)
        elif(d==2):
            a.append(m)
        elif(d==3):
            b=int(input("Enter at which index(Starting from 1):"))
            a.insert(b,m)
        else:
            print("Invalid input plz try again")
            
            
        
    elif(c==2):
        print("Do you wish to:\n1. Deleting the first node\n 2.Deleting the last node \n 3.Deleting the node at any giving index")
        d=int(input())
        if(d==1):
            a.deletion(1)
        elif(d==2):
            a.deletion(a.len())
        elif d==3:
            m=int(input("Enter the index(starting from 1):"))
            a.deletion(m)
        else:
            print("Invalid input plz try again")
    elif(c==3):
        a.display()
    elif(c==4):
        m=int(input("Enter the value:"))
        a.search(m)
        
    elif(c==5):
        print("Terminating program")
        break
    
        