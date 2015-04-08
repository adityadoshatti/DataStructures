class List:
    def __init__(self):
        self.item=[]
    def add(self,data):
        k=len(self.item)
        self.item.insert(k+1,data)
    def rem(self,data):
        if data in self.item:
            self.item.remove(data);
        else:
            print "Invalid Data"
    def disp(self):
        print self.item
l=List()
while(1):
    print "1.Add In Linked List"
    print "2.Remove Data Item"
    print "3.Display"
    print "4.Exit"
    n=int(raw_input())
    if n==1:
        print "Enter Value to be added:"
        data=int(raw_input())
        l.add(data)
    elif n==2:
        print "Enter Value to be removed:"
        data=int(raw_input())
        l.rem(data)
    elif n==3:
        print l.disp()
    else:
            break
