# ALL THE LOGIC NEEDED FOR HASHTABLE

# array of 8 items, all None
hash_table = [None] * 8
​
# ​Defining a LL class with key and value for a hash table
class HashTableItem:
     def __init__(self, key, value, next=None):
         self.key = key
         self.value = value
         self.next = next
        
​
​
# ​Hashing Function
def my_hash(s):
    s_utf8 = s.encode()
​
    total = 0
​
    for c in s_utf8:
        total += c
​
    return total
# ​insert key value
def put(key, value):
    hashed_key = my_hash(key)
​
    index = hashed_key % len(hash_table)
​
    # print a warning if we are going to overwrite
    
    if hash_table[index] != None:
        print('omg think of the data!')
​
    hash_table[index] = HashTableItem(key, value)
# ​retrieve key value
def get(key):
    hashed_key = my_hash(key)
    index = hashed_key % len(hash_table)
​
    table_item = hash_table[index]
​
    return table_item.value


def delete(key):
    hashed_key = my_hash(key)
    index = hashed_key % len(hash_table)
    hash_table[index] = None
​
put("hello", "hello world")
​
put("olleh", "we didnt start the fire")
​
print(get("hello"))
​
print(hash_table)
​
delete("hello")
print(hash_table)
​
# [None, None, None, None, 'hello world', 'we didnt start the fire', None, None]
# [None, None, None, None, None, None, None, None]



# Basic LL with value(just refresher)
class ListNode:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

def find(self,value):
    # traverse node and find the value
    curr =self.head:
    while curr.next is not None:
          if curr.value == value:
              return current
           curr = curr.next
    # If we dont find the value we are looking for  then return None
    return None          


def insert_at head(self,value):
    node=ListNode(value)
    # insert in empty LL(no head)
    if self.head is None:
        self.head=node
    else:
        curr=self.head
        node.next=curr
        self.head=node 

def delete(self,value):
    curr=self.head
    
    # 1. if there is nothing to delete
    if curr is None:
        return None
    # if head has the value to be deleted 
    if curr.value=value:
        self.head= curr.next
        return current 
    # when deleting something else
    else:
        prev=curr
        curr=curr.next
        while curr is not None:
            if curr.value== value:
                prev.next=curr.next
                return curr #return our deleted node
            else:
                # move one step forward and update pointers
                prev=curr
                curr=curr.next
        return None #couldn't find the value we were looking for            
