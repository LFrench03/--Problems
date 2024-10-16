#380 Insert Delete GetRandom O(1)
'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not presultent. Returns true if the item was not presultent, false otherwise.
bool remove(int val) Removes an item val from the set if presultent. Returns true if the item was presultent, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''
import random
class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
    def insert(self, val: int) -> bool:
        if val not in self.list: return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict: return False
        last_element = self.list[-1]
        idx_to_remove = self.dict[val]
        self.list[idx_to_remove] = last_element
        self.dict[last_element] = idx_to_remove        
        self.list.pop()
        del self.dict[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.list)