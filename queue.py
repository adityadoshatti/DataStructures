class Node(object):
     def __init__(self, data):
         self.data = data
         self.next = None
class Queue():
    def __init__(self,top=None):
        self.top = top
        self.size = 0
    def enqueue(self,node):
        if self.top==None:
            self.top=node
            self.size=self.size+1
        else:
            self.size=self.size+1
            node1=self.top
            while(node1.next!=None):
                node1=node1.next
            node1.next=node
    def Dequeue(self):
        if self.top==None:
            print "Nothing to Remove"
        else:
            temp=self.top.data
            self.size=self.size-1
            self.top=self.top.next
            return temp
    def len(self):
        return self.size 
    def display(self):
        if self.top==None:
            print "Nothin to Print"
        else:
            temp=self.top
            while temp!=None:
                print temp.data
                temp=temp.next
q=Queue()    
while(1):
    print "1.Enqueue"
    print "2.Pop"
    print "3.Queue Length"
    print "4.Print Queue"
    print "5.Exit"
    print "Option:"
    n=int(raw_input())
    if n==1:
        print "Enter Value to be added:"
        data=int(raw_input())
        n=Node(data)
        q.enqueue(n)
    elif n==2:
        print q.Dequeue()
    elif n==3:
         print q.len()
    elif n==4:
        q.display()
    else:
        break
