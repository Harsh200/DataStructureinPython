class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None


class Linkedlist():
    def __init__(self):
        self.headval=None


    def listprint(self):
       printval=self.headval
       while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

list1=Linkedlist()
list1.headval=Node("Mon")
e2=Node("tue")
e3=Node("wed")
list1.headval.nextval=e2
e2.nextval=e3

list1.listprint()