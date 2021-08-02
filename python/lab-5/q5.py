class node:
    def __init__(self,data=None):
        self.left=None
        self.right=None
        self.data=data
class tree:
    def __init__(self):
        self.root=node()
        
    def insertion(self,data):
        new_node=node(data)
        if self.root.data==None:
            self.root=new_node
        else: 
            cur_node=self.root
            while True:
                if cur_node.data>data:
                    if cur_node.left==None:
                        break
                    cur_node=cur_node.left
                else:
                    
                    if cur_node.right==None:
                        break
                    cur_node=cur_node.right
            if cur_node.data>data:
                cur_node.left=new_node
            else:
                cur_node.right=new_node

    
    
    def display(self,n):
        
        
a=tree()

a.insertion(20)
a.insertion(10)
a.insertion(30)
a.insertion(40)
a.display()