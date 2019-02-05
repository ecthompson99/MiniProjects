from json import dumps, loads

products = []
quit = True
counter = 1

class Product:
    def __init__(self, name, price, description): 
        self.name = name
        self.price = price
        self.description = description
        self.dict = {"name": self.name, "price": self.price, "description": self.description}

def list(products):
    if len(products) == 0: 
        print("Inventory is empty")
    for p in products: 
        print("Product: {}, Price: ${}, Description: {}".format(p.name, p.price, p.description))

try:
    load_inventory = open('inventory.json', 'r+')
    inventory_list = loads(load_inventory.read())
    for i in inventory_list: 
        products.append(Product(i["name"], i["price"], i["description"]))
except:
    pass

inventory_file = open('inventory.json', 'w+')

while quit:
    while counter == 1: 
        print("\nTYPE: \n{:>10} to add a product; \n{:>10} to show inventory; \n{:>10} for total assets; \n{:>10} to clear inventory; \n{:>10} to exit.".format("'add'", "'list'", "'total'", "'clear'", "'quit'"))
        counter += 1
        
    init_prompt = input("Please type your command (Type 'commands' for help): ")
    
    if init_prompt == "add": 
        name = input("What is the name of your product?: ")
        price = input("What is the price of your product?: ")
        description = input("How would you describe your product?: ")
        products.append(Product(name, price, description))

    elif init_prompt == "list": 
        list(products)
    
    elif init_prompt == "total": 
        print(sum([float(i.price) for i in products]))
        
    elif init_prompt == "clear": 
        products.clear()
        
    elif init_prompt == "commands": 
        counter = 1
        
    elif init_prompt == "quit":
        inventory_file.write(dumps([i.dict for i in products]))
        quit = False
    else: 
        print("\nPlease enter a valid command to continue.")