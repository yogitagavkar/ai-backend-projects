class OrderManager:
    def __init__(self):
        self.items = []
        self.tax_rate = 0.08
        self.tip = 0
        self.discount = 0

    def add_item(self, name, qty, price, modifiers=None):
        line_total = qty * price

        item = {
            "name": name,
            "qty": qty,
            "unit_price": price,
            "modifiers": modifiers or [],
            "line_total": line_total
        }

        self.items.append(item)

        return f"Added {qty} x {name}"

    def calculate_bill(self):
        subtotal = sum(i["line_total"] for i in self.items)
        tax = round(subtotal * self.tax_rate, 2)
        total = subtotal + tax + self.tip - self.discount

        return {
            "items": self.items,
            "subtotal": subtotal,
            "tax": tax,
            "tip": self.tip,
            "discounts": self.discount,
            "total": total
        }