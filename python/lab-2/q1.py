import array

class int_array:
    def __init__(self,arr1):
        self.a=arr1
        
    def error_stat(self,message):
        print(message+"plz try again")
        
    def Trav_function(self):
        print(*self.a)
        
    def insertion(self,index,value):
        if index>len(self.a):
            error_stat("Invalid index")
            return
        self.a.insert(index,value)
        
        
    def insertion_end(self,value):
        self.a.append(value)
        
        
    def rem_value(self,value):
        if value not in self.a:
            error_stat("Value not found")
            return
        self.a.remove(value)
        
    def rem_index(self,index):
        if index>len(self.a):
            error_stat("Invalid index")
            return 
        self.a.pop(index)
        

        
    def search_val(self,value):
        if value not in self.a:
            error_stat("Value not found.")
            return
        print(self.a.index(value))
    
    def search_index(self,index):
        if index>len(self.a):
            error_stat("Invalid index")
            return
        print(a[index])


arr1=array.array('i',[])
n=int(input("Enter the length of the array:"))
for i in range(n):
    arr1.append(int(input("Enter a integer for the array:")))
a=int_array(arr1)
while(True):
    print("Select an option\n 1. Inserting elements in the array \n 2. deleting elements in the array \n 3. displaying the elements in the array \n 4. searching an element in the array\n 5.exit the program\n")
    c=int(input())
    
    
    if(c==1):
        print("Do you wish to:\n 1. insert at the beginning \n 2. insert at the end \n 3. insert at some index\n")
        d=int(input())
        m=int(input("The value u wish to insert:"))
        if(d==1):
            a.insertion(0,m)
        elif(d==2):
            a.insertion_end(m)
        elif(d==3):
            b=int(input("Enter at which index do u wish to insert the value:"))
            a.insertion(b,m)
        else:
            print("Invalid input plz try again")
            
            
            
    elif(c==2):
        print("Do you wish to:\n1. Deletion elements by index \n2. Deletion elements by value\n")
        d=int(input())
        m=int(input("Enter the index or value u opted to remove:"))
        if(d==1):
            a.rem_index(m)
        elif(d==2):
            a.rem_value(m)
        else:
            print("Invalid input so try again")
    elif(c==3):
        a.Trav_function()
    elif(c==4):
        d=int(input("Do you wish to:\n 1.search by value\n 2. search by index\n"))
        m=int(input("Enter the index or value u want to search:"))
        if d==1:
            a.search_val(m)
        elif d==2:
            a.search_index(m)
        else:
            print("Invalid value so plz try again")
    elif(c==5):
        print("Terminating program")
        break
        
        
        