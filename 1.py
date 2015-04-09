class Node(object):
     def __init__(self, data):
         self.data = data
         self.next = None
class LinkedList():
    def __init__(self,head=None):
        self.head = head
    def insert(self,node):
        if self.head == None:
            self.head=node
        else:
            node.next = self.head
            self.head=node
    def delete(self,node):
        if self.head==None:
            print "Not in the list"
        else:
            i=self.head
            p=None
            f=0
            while f!=1:
                if i == None:
                    print "Not in the list"
                    break 
                elif i.data == node.data:
                    f=1
                else:
                    p=i
                    i=i.next
            if f==1:
                if p==None:
                    self.head=i.next
                else:
                    p.next=i.next
    def display(self):
        m=self.head
        while m!=None:
            print m.data
            m=m.next
ll=LinkedList()    
while(1):
    print "1.Add In Linked List"
    print "2.Remove Data Item"
    print "3.Display"
    print "4.Exit"
    n=int(raw_input())
    if n==1:
        print "Enter Value to be added:"
        data=int(raw_input())
        n=Node(data)
        ll.insert(n)
    elif n==2:
        print "Enter Value to be removed:"
        data=int(raw_input())
        n=Node(data)
        ll.delete(n)
    elif n==3:
        print ll.display()
    else:
        break
