class InvalidSalesItemError(Exception):
    """Represents an error when an input sales item is not in the system"""
    pass

class SalesItem:
    """Represents an item for sale with a name, wholesale cost, and selling price"""

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


class SalesForDay:
    """Represents the sales at a business for a particular day"""

    def __init__(self, days, sales_dict):
        """Creates a new sales for day object that specifies a particular day and a dictionary with the names and amounts of the items sold"""
        self._days = days
        self._sales_dict = sales_dict

    def get_day(self):
        """Returns the number of days the lemonade stand has been open so far"""
        return self._days

    def get_sales_dict(self):
        """Returns a dictionary whose keys are the names of the items sold and whose values are the number of those items sold"""
        return self._sales_dict