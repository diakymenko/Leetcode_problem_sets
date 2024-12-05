import random
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.ids = []
        

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.ids)
      
        self.ids.append(val)
       
        return True
        

    def remove(self, val: int) -> bool:
        if not val in self.map:
            return False
        
          # delete from list
        last_val = self.ids[-1]
        idx_val_to_remove = self.map[val]

        self.ids[idx_val_to_remove] = last_val
        self.ids.pop()

        self.map[last_val] = idx_val_to_remove
        del self.map[val]
        return True


        
    def getRandom(self) -> int:
        return random.choice(self.ids)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()