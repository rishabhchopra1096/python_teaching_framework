# ice_cream_data.py
# This is where students learn core Python concepts!

# Start with a simple dictionary to store our ice cream data
ice_cream_flavors = {
    "Vanilla": {
        "description": "Classic, creamy vanilla bean",
        "price": 2.99,
        "ingredients": ["vanilla bean", "cream", "sugar"]
    }, 
    "Chocolate": {
        "description": "Rich, dark chocolate",
        "price": 3.49,
        "ingredients": ["cocoa", "cream", "sugar"]
    }
}

# Function to add a new flavor - teaches dictionary operations
def add_new_flavor(name, description, price, ingredients):
    ice_cream_flavors[name] = {
        "description": description,
        "price": price,
        "ingredients": ingredients
    }

# Function to change a price - teaches how to update nested dictionary values
def change_price(flavor_name, new_price):
    if flavor_name in ice_cream_flavors:
        ice_cream_flavors[flavor_name]["price"] = new_price

# Function to remove a flavor - teaches dictionary deletion
def remove_flavor(flavor_name):
    if flavor_name in ice_cream_flavors:
        del ice_cream_flavors[flavor_name]