class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
        
class Stack:
    def __init__(self):
        self.head=Node()
        
    def append(self,dataval):
        newnode=Node(dataval)
        cursor=self.head
        while cursor.nextval != None:
            cursor=cursor.nextval
        cursor.nextval=newnode
        
    def pop(self):
        cursor=self.head
        while cursor.nextval != None:
            prevnode=cursor
            cursor=cursor.nextval
        val=prevnode.dataval
        prevnode.nextval=None
        print("Popped value:",val)
        return val
    
    def display(self):
        cursor=self.head
        ls=[]
        while cursor.nextval != None:
            cursor=cursor.nextval
            ls.append(cursor.dataval)
        print("Stack:",ls)
        return ls
            
    
s=Stack()
s.append(1)
s.append(2)
s.append(3)
s.append(4)
s.display()
s.pop()
s.display()