class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

# measure of how full the hash table is allowed to get before its capacity is increased. 
HI_THRESHOLD = 0.70

# measure of how empty the hash table is allowed to get before its capacity is decreased. 
LO_THRESHOLD = 0.20

# implemented as an array - each element of which is a LinkedList of HashTableEntry objects
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity=capacity
        self.storage=[None]*capacity
        self.num_items =0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # start from a large prime number
        hash_value=5381

        for char in key:
            hash_value=hash_value+(hash_value << 5)+ ord(char)
        return hash_value       

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # index is stored as the return value of the hashing function
        index = self.hash_index(key)
        
        # there is no LL at the index
        if self.storage[index] is None:
            # put the LL node at that index of array
            self.storage[index] = HashTableEntry(key, value)
            self.num_items += 1
            
            # having added a new entry, let's check the hi threshold
            if self.get_load_factor() > HI_THRESHOLD:
                self.resize(self.capacity * 2)

        # if something already exists ie value at index is not None 
        else:
            # get the head node
            node = self.storage[index]

            # In case of hash collision, traverse LL and find the node with the matching key or end of LL 
            while node.key != key and node.next is not None:
                node = node.next
            
            # if we found the node with matching key
            if node.key == key:
                # if key already exists , then overwrite the value
                node.value = value
            else:
                # we didn't find the node with matching key, so we are at end of LL
                node.next = HashTableEntry(key, value)
                self.num_items += 1
                

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index] is None:
            return None
        else:
            node = self.storage[index]
            prev = None

            # In case of hash collision, traverse LL and find the node with the matching key or end of LL 
            while node.key != key and node.next is not None:
                prev = node
                node = node.next

            # if we found the node with matching key
            if node.key == key:
                # if it's a head node
                if prev is None:
                    # move head pointer to next node and store reference in array
                    self.storage[index] = node.next
                else:
                    # if not a head, then link prev node to next node, removing current node from the LL
                    prev.next = node.next

                if self.storage[index] is None:
                    self.num_items -= 1
                    
                    # having deleted an entry, let's check the lo threshold
                    if self.get_load_factor() < LO_THRESHOLD and self.capacity >= 2*MIN_CAPACITY:
                        self.resize(self.capacity // 2)

                # return the value corresponding to deleted key
                return node.value
            else:
                # we didn't find the node to delete
                return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Find the index using the key
        index = self.hash_index(key)
        #  if there is nothing at that index
        if self.storage[index] is None:
            return None
        else:
            node = self.storage[index]
            
            # In case of hash collision, traverse LL and find the node with the matching key or end of LL 
            while node.key != key and node.next is not None:
                node = node.next

            # if we found the node with matching key
            if node.key == key:
                return node.value
            else:
                return None    


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        new_hash_table = HashTable(new_capacity)

        for node in self.storage:
            if node:
                new_hash_table.put(node.key, node.value)

        self.storage = new_hash_table.storage
        self.capacity = new_hash_table.capacity
        self.num_items = new_hash_table.num_items

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
