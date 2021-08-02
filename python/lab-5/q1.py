class node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
class tree:
    def __init__(self):
        self.root=node("+")
        self.s=""
    def insertion(self,u,v,w,x,y,z):
        self.root.left=node("-")
        cur_node=self.root.left
        cur_node.left=node("+")
        cur_node.right=node(w)
        cur_node=cur_node.left
        cur_node.left=node(x)
        cur_node.right=node("*")
        cur_node=cur_node.right
        cur_node.left=node(y)
        cur_node.right=node(z)
        
        self.root.right=node("-")
        cur_node=self.root.right
        cur_node.left=node(u)
        cur_node.right=node(v)
        
    def display(self,cur_node):
        if cur_node.left.left!=None:
            self.display(cur_node.left)
        else:
            self.s+="("+cur_node.left.data
        self.s+=cur_node.data
        if cur_node.right.right!=None:
            self.display(cur_node.right)
        else:
            self.s+=cur_node.right.data+")"
        
a=tree()
print("Enter the values for u,v,w,x,y,z:")
u,v,w,x,y,z=input().split()
a.insertion(u,v,w,x,y,z)
a.display(a.root)
print(a.s)
print(eval(a.s))