class Shop:
    amount_of_items = 0

    def __init__(self, name, items):
         self.name = name
         self.items = list(items)

    def get_items_count(self):
        self.amount_of_items = len(self.items)
        return self.amount_of_items


# Test code:


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())


# Expected output: '3'