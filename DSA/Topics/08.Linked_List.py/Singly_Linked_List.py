class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linked_List:
    def __init__(self):
        self.head=None

    def list_to_linked_list(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data)
        
    def insert_at(self,data,index):
        if index<0 or index>=self.get_len():                # 1-->3-->7-->9-->None
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_beginning(data)
            return 
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break

            itr=itr.next
            count+=1
    def remove_at(self,index):
        if index<0 or index >= self.get_len():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        count=0   
        itr=self.head
        while itr:
            if count==index-1:
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
        return(count)

    def print_list(self):
        if self.head is None:
            print("Linked List is Empty")
            return 
        
        list_str=""
        itr=self.head
        while itr:
            list_str+=str(itr.data)+"-->"
            itr=itr.next
        print(list_str+"None")
            



linked_list=Linked_List()
linked_list.list_to_linked_list([1,2,4,7,9])
linked_list.insert_at_beginning(0)
linked_list.insert_at_end(10)
linked_list.insert_at(3,3)
linked_list.insert_at(5,5)
linked_list.remove_at(0)
linked_list.print_list()
print(linked_list.get_len())
