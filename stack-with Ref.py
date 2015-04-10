class Node(object):
     def __init__(self, data):
         self.data = data
         self.next = None
class Stack():
    def __init__(self,top=None):
        self.top = top
        self.size = 0
    def push(self,node):
        if self.top==None:
            self.top=node
            self.size=self.size+1
        else:
            self.size=self.size+1
            node.next=self.top
            self.top=node
    def pop(self):
        if self.top==None:
            print "Nothing to Pop"
        else:
            temp=self.top.data
            self.size=self.size-1
            self.top=self.top.next
            return temp
    def topCall(self):
        return self.top.data
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
S=Stack()    
while(1):
    print "1.Push"
    print "2.Pop"
    print "3.Print Top"
    print "4.Get Length"
    print "5.Print Stack"
    print "6.Exit"
    print "Option:"
    n=int(raw_input())
    if n==1:
        print "Enter Value to be added:"
        data=int(raw_input())
        n=Node(data)
        S.push(n)
    elif n==2:
        print S.pop()
    elif n==3:
        print S.topCall()
    elif n==4:
         print S.len()
    elif n==5:
        S.display()
    else:
        break
