class InvalidSalesItemError(Exception):
    """Represents an error when an input sales item is not in the system"""
    pass

class SalesItem:
    """Represents an item for sale on the Nonopet website with a name, wholesale cost, and selling price"""

    def __init__(self, name, cost, price):
        """Creates a new menu item with a specified name, wholesale cost, and selling price"""
        self._name = name
        self._cost = cost
        self._price = price

    def get_name(self):
        """Returns item name"""
        return self._name

    def get_wholesale_cost(self):
        """Returns item cost"""
        return self._cost

    def get_selling_price(self):
        """Returns item price"""
        return self._price
