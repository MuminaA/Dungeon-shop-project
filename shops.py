class Shop:
    def __init__(self, name, gold_amount, items, item_amount):
        self.name = name
        self.gold_amount = gold_amount
        self.items = items
        self.item_amount = item_amount

    def removeItems(self, items):
        if not items:
            return None, []
        removed = items.pop(0)
        return removed, items

    def increaseGold(self, gold_amount, item_amount):
        total_amount = gold_amount + item_amount
        return total_amount
    
    def details(self):
        current_amount = self.increaseGold(self.gold_amount, self.item_amount)
        sold_item, current_items = self.removeItems(self.items)

        print(f"{self.name} sold a {sold_item} for {self.item_amount} gold coins.")
        print(f"Gold is now: {current_amount}")
        print(f"items left: {current_items}")