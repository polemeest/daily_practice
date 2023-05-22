class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items = items_per_page
        self.length = len(self.collection)

    # returns the number of items within the entire collection
    def item_count(self):
        return self.length

    # returns the number of pages
    def page_count(self):
        if self.collection:
            return self.length // self.items + 1 if self.length % self.items > 0 else self.length // self.items
        return 0

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        print(f'{self.collection} len={self.length} per page={self.items} ind={page_index} total={self.page_count()}')
        if page_index < 0 or page_index > self.page_count() - 1:
            return -1
        elif page_index == self.page_count() - 1 and self.length > self.items:
            return len(self.collection[self.items * page_index::])
        else:
            return min(self.items, self.length)

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if -1 <= item_index < self.length and self.collection:
            return item_index // self.items if self.items else -1
        return -1