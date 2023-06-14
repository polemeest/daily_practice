# from random import choice
# class RandomizedSet():

#     def __init__(self):
#         self.set = dict()


#     def insert(self, val: int) -> bool:
#         if val not in self.set:
#             self.set[val] = ''
#             return True
#         return False


#     def remove(self, val: int) -> bool:
#         if val in self.set:
#             del self.set[val]
#             return True
#         return False

#     def getRandom(self) -> int:
#         return choice(list(self.set))


from random import choice
class RandomizedSet():

    def __init__(self):
        self.map = dict()
        self.list = list()


    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.list)
            self.list.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val in self.map:
            self.map[self.list[-1]] = self.map[val]
            self.list[self.map[val]], self.list[-1] = self.list[-1], self.list[self.map[val]]
            del self.map[val]
            self.list.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)



a = b = c = RandomizedSet()

for i in range(10):
    a.insert(i)

for i in range(5):
    a.remove(i)

print(a.getRandom())