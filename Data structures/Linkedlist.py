class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class linkedlist:
    def __init__(self):
        self.head=Node()
        
    def append(self,dataval):
        newnode=Node(dataval)
        cursor=self.head
        while cursor.nextval != None:
            cursor=cursor.nextval
        cursor.nextval=newnode
        
    def display(self):
        ls=[]
        cursor=self.head
        while cursor.nextval != None:
            cursor=cursor.nextval
            ls.append(cursor.dataval)
        print(ls)
        return ls
    
    def len(self):
        cursor=self.head
        count=0
        while cursor.nextval!=None:
            cursor=cursor.nextval
            count+=1
        print(count)
        return count
    
    def remove(self,index):
        if index >= self.len():
            print("Index out of range")
            return None
        curid=0
        cursor=self.head
        while curid != index:
            prevnode=cursor
            cursor=cursor.nextval
            curid+=1
        prevnode.nextval=cursor.nextval
        
        

ls=linkedlist()
ls.append(0)
ls.append(1)
ls.append(2)
ls.append(3)
ls.append(4)
ls.display()
ls.remove(3)
ls.display()