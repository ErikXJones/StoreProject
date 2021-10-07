# Author: Quynh Nguyen
# Date: October 6th, 2021
# Description: The program is an store stimulator where store members and premium members can search and purchase products.

# create InvalidCheckoutError as a class that inherits from Exception
class InvalidCheckoutError(Exception):
    # to tell python interpreter that the body is empty
    pass


# create class Product definition
class Product:
    """
    A class to represent a Product

    Attributes:
        product_id (str): product's ID
        title (str): name of product
        description (str): description of product
        price (float): price of product
        quantity_available (int): quantity of product available
    """

    # init method to initialize data members
    def __init__(self, product_id, title, description, price, quantity_available):
        """
        Constructor for Product class

            Parameters:
                product_id (str): product's ID
                title (str): name of product
                description (str): description of product
                price (float): price of product
                quantity_available (int): quantity of product available
        """
        # create private data members
        self._product_id = product_id
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    # method to get product's ID
    def get_product_id(self):
        """Returns the product's ID"""
        return self._product_id

    # method to get title
    def get_title(self):
        """Returns the product's title"""
        return self._title

    # method to get description
    def get_description(self):
        """Returns the product's description"""
        return self._description

    # method to get price
    def get_price(self):
        """Returns the product's price"""
        return self._price

    # method to get quantity available
    def get_quantity_available(self):
        """Returns the product's quantity available"""
        return self._quantity_available

    # method to decrease product's quantity
    def decrease_quantity(self):
        # decrease quantity available by 1
        self._quantity_available -= 1


# create class Customer definition
class Customer:
    """
    A class to represent a Customer

        Attributes:
            name (str): name of customer
            customer_id (str): customer's ID
            premium_member (boolean): if customer is a premium member
    """

    # init method to initialize data members
    def __init__(self, name, customer_id, premium_member):
        """
        Constructor for Customer class

            Parameters:
                name (str): name of customer
                customer_id (str): customer's ID
                premium_member (boolean): if customer is a premium member
        """
        # create private data members
        self._name = name
        self._customer_id = customer_id
        self._premium_member = premium_member
        # list of product ID codes
        self._cart = []

    # method to get cart
    def get_cart(self):
        """Returns the customer's cart"""
        return self._cart

    # method to get name
    def get_name(self):
        """Returns the customer's name"""
        return self._name

    # method to get customer's ID
    def get_customer_id(self):
        """Returns the customer's ID"""
        return self._customer_id

    # method to determine if customer is premium member
    def is_premium_member(self):
        """Returns whether customer is premium member or not"""
        if self._premium_member:
            return True
        else:
            return False

    # method to take product ID
    def add_product_to_cart(self, product_id):
        # add to customer's cart
        self._cart.append(product_id)

    # method to empty customer's cart
    def empty_cart(self):
        self._cart = []


# create class Store definition
class Store:
    """
    A class to represent the Store

        Attributes:
            inventory: list of products
            membership: list of customers that are members of the store
    """

    # init method to initialize data members
    def __init__(self):
        """
        Constructor for Store class

            Parameters:
                inventory: list of products
                membership: list of customers that are members of the store
        """
        # list of inventory, membership
        self._inventory = []
        self._membership = []

    # method to take product ID
    def add_product(self, product):
        # add to inventory
        self._inventory.append(product)

    # method to take customer object
    def add_member(self, customer):
        # add to membership
        self._membership.append(customer)

    # method to take find matching product's ID
    def lookup_product_from_id(self, product_id):
        # for product in inventory
        for product in self._inventory:
            # if loop to match product with product ID
            if product.get_product_id() == product_id:
                """Returns product with matching ID"""
                return product
        """Returns None if there is no matching ID found"""
        return None

    # method to take find matching customer's ID
    def lookup_member_from_id(self, customer_id):
        # for member in store's membership
        for member in self._membership:
            # if loop to match member with customer ID
            if member.get_customer_id() == customer_id:
                """Returns member with matching ID"""
                return member
        """Returns None if there is no matching ID found"""
        return None

    # method to search products and return sorted list of product's ID
    def product_search(self, search_string):
        # list of product ID's
        product_id_list = []
        # for products in inventory
        for products in self._inventory:
            # if loop to match strings given title or description
            # convert search string to all lowercase
            if search_string.lower() in products.get_title() \
                    or search_string.lower() in products.get_description():
                # add to product's ID list if products match string
                product_id_list.append(products.get_product_id())
                # if search string is not found
                # sort list in lexicographic order
                product_id_list.sort()
                """Returns list of product's ID codes"""
                return product_id_list
            else:
                """Returns empty list"""
                return []

    # method to add product to cart if found in inventory and customer is a member
    def add_product_to_member_cart(self, product_id, customer_id):
        # if product is not found in inventory
        if product_id not in self._inventory:
            return "product ID not found"
        # if customer is not found in membership
        if customer_id not in self._membership:
            return "member ID not found"
        # if both product and customer is found
        if product_id.get_quantity_avaliable() > 0 and customer_id.add_product_to_cart():
            return "product added to cart"
        # if both product and customer is not found
        else:
            return "product out of stock"

    # method to check out given customer's ID
    def check_out_member(self, customer_id):
        x = self.lookup_member_from_id(customer_id)
        # if loop to check if customer is a member
        if x in self._membership:
            for customer in self._membership:
                # set variables
                total_cost = 0
                running_total = 0
                for product_id in customer.get_cart():
                    self.lookup_product_from_id(product_id)
                    # make sure product is in stock
                    product_id.get_quantity_available() > 0
                    # calculate total cost
                    total_cost = product_id.get_price()
                    # decrease product's quantity by 1
                    product_id.decrease_quantity()
                    # if loop to see if customer is a premium member
                    if customer.is_premium_member():
                        total_cost = running_total
                    # if member is not premium member, add 7% shipping cost
                    else:
                        total_cost += 0.07 * running_total
                # empty customer cart
                customer.empty_cart()
                """Returns total cost + shipping cost"""
                return total_cost
        # if customer ID does not match member of the Store
        else:
            # raise Exception
            raise InvalidCheckoutError()


# main function for file that is run as a script
def main():
    p1 = Product("889", "Rodent of unusual size",
                 "when a rodent of the usual size just won't do", 33.45, 8)
    c1 = Customer("Yinsheng", "QWF", False)
    myStore = Store()
    myStore.add_product(p1)
    myStore.add_member(c1)
    myStore.add_product_to_member_cart("889", "QWF")
    # try block that might raise an exception
    try:
        result = myStore.check_out_member("QWF")
        print("Total cost: $", result)
    # specify which exception is being handled
    except InvalidCheckoutError:
        print("Member ID Not Found. Please try again.")
    # runs whether an exception was raised or not
    finally:
        print("Thank you for coming!")


# determines whether main function gets called
if __name__ == "__main__":
    main()
