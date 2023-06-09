class User():
    ranks = [i for i in range(-8, 9) if i != 0]

    def __init__(self):
        self.rank = -8
        self.progress = 0


    def inc_progress(self, rank):
        if rank not in self.ranks:
            raise IndexError('rank is beyond limit')
        if self.rank >= 8:
            pass
        else:
            diff = self.ranks.index(rank) - self.ranks.index(self.rank)
            self.add_points(diff)
            self.calc_progress()



    def calc_progress(self):
        if self.progress >= 100:
            self.rank = self.ranks[self.ranks.index(self.rank) + self.progress // 100]
            self.progress = self.progress % 100 if self.rank < 8 else 0


    def add_points(self, diff):
        if diff < -1:
            pass
        elif diff == -1:
            self.progress += 1
        elif diff == 0:
            self.progress += 3
        else:
            self.progress += 10 * diff * diff