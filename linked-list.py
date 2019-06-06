# linked list example

# the node calss
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def get_data(self):
        return self.val
    def set_data(self,val):
        self.val = val
    def get_next(self):
        return self.next
    def set_next(self,next):
        self.next = next
        
# the linkedlist class
class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
        self.count = 0
        
    def get_count(self):
        return self.count
    # to insert new node
    def insert(self,data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count +=1
        
    #finding a value
    def find(self,val):
        item = self.head
        while (item != None):   # to check till the item is last
            if item.get_data() == val:  # if the item given as input matched the item in list
                return item             # returns the item
            else:
                item = item.get_next() # if it dosent match, we go to the next item
        return None
    # function to delete at particular location
    def deleteAt(self, index):
        if index > self.count:      # if the given index/position is larget than the list size. retun nothing
            return
        if self.head == None:    # if the 
            return
        else:
            tempIndex = 0
            node = self.head
            while tempIndex < index-1:
                node = node.get_next()
                tempIndex +=1
            node.set_next(node.get_next().get_next())
            self.count -=1
            
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()
            
            
    # create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)

itemlist.dump_list()

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()

    
        