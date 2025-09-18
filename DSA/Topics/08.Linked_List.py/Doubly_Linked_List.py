class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class Doubly_Linked_List:
    def __init__(self):
        self.head=None

    def list_to_linked_list(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_beginning(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        node=Node(data,None,self.head)
        self.head=node
        self.head.next.prev=self.head

    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data)
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        node=Node(data,itr)
        itr.next=node

    def insert_at(self,data,index):
        if index<0 or index>self.get_len():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_beginning(data)
            return 
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr,itr.next)
                if itr.next:
                    itr.next.prev=node
                itr.next=node
                break
            itr=itr.next
            count+=1

    def remove_at(self,index):
        if index<0 or index>self.get_len():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        if index==(self.get_len()-1):
            itr=self.head
            while itr.next:
                itr=itr.next
            itr.prev.next=None
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next.next.prev=itr
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def get_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def print_list(self):
        itr=self.head
        list_str=""
        while itr:
            list_str+=str(itr.data)+" <--> "
            itr=itr.next
        print(list_str+"None")      #"None <--> "+   
dll=Doubly_Linked_List()
dll.list_to_linked_list([1,2,5,7])
dll.insert_at_beginning(1)
dll.insert_at_beginning(6)
dll.insert_at_beginning(4)
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at(100,1)
dll.remove_at(1)
            
dll.remove_at(2)
dll.remove_at(0)
dll.print_list()
print(dll.get_len())