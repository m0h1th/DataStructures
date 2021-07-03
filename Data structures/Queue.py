class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
        
class Queue:
    def __init__(self):
        self.head=Node()
        
    def append(self,dataval):
        newnode=Node(dataval)
        cursor=self.head
        while cursor.nextval != None:
            cursor=cursor.nextval
        cursor.nextval=newnode
        
    def popleft(self):
        cursor=self.head
        cursor=cursor.nextval
        if cursor.dataval != None:
            val=cursor.dataval
            print("Popped value:",val)
            nextnode=cursor.nextval
            cursor=self.head
            cursor.nextval=nextnode
            return val
        else:
            print("Empty queue")
            return None
    
    def display(self):
        cursor=self.head
        ls=[]
        while cursor.nextval != None:
            cursor=cursor.nextval
            ls.append(cursor.dataval)
        print("Stack:",ls)
        return ls
    
q=Queue()
q.append(0)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.display()
q.popleft()
q.display()
q.popleft()
q.display()