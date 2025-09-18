class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Circular_Linked_List:
    def __init__(self):
        self.head=None

    def list_to_linked_list(self,data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        if self.head is None:
            self.head=node
            self.head.next=node
            return
        itr=self.head
        while itr.next!=self.head:
            itr=itr.next
        itr.next=node
        self.head=node
    
    def insert_at_end(self,data):
        node=Node(data,self.head)
        if self.head is None:
            self.head=node
            self.head.next=node
            return
        itr=self.head
        while itr.next!=self.head:
            itr=itr.next
        itr.next=node
        
    def insert_at(self,data,index):
        if index<0 or index>=self.get_len():                
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_beginning(data)
            return 
        count=0
        itr=self.head
        while itr.next!=self.head:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break

            itr=itr.next
            count+=1
    def remove_at(self,index):
        if index<0 or index >=self.get_len():
            raise Exception("Invalid Index")
            
        if index==0:  
            if self.head.next == self.head:  
                self.head = None
                return                  
            itr=self.head
            while itr.next!=self.head:
                itr=itr.next
            itr.next=self.head.next
            self.head=self.head.next
        count=0             
        itr=self.head
        while itr.next!=self.head:
            if count==index-1:
                itr.next=itr.next.next

                break
            itr=itr.next
            count+=1


    def print_list(self):
        if self.head is None:
            print("Empty List")
            return
        list_str=""
        itr = self.head
        while itr:
            list_str+=str(itr.data)+" --> "
            itr = itr.next
            if itr == self.head:
                itr=None
        print(list_str)

    def get_len(self):
        count=0
        itr=self.head       # 1-->2-->3-->4-->
        while itr:
            count+=1
            if itr.next==self.head:
                break
            itr=itr.next
            
        return count
cll=Circular_Linked_List()
cll.list_to_linked_list([10,20,30,40])
cll.insert_at_beginning(5)
cll.insert_at_beginning(0)
cll.insert_at_end(80)
cll.insert_at_end(90)
cll.insert_at(7,2)
cll.insert_at(85,8)
cll.remove_at(0)
cll.remove_at(8)
cll.remove_at(5)
cll.print_list()
print(cll.get_len())
