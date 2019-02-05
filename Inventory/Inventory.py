class Products:
    def __init__(self, name, price, description): 
        self.name = name
        self.price = price
        self.description = description

quit = True
while quit: 
    init_prompt = input("Type 'add' to add a product, 'quit' to exit: ")
    if init_prompt == "add": 
        name = input("What is the name of your product?: ")
        price = input("What is the price of your product?: ")
        description = input("How would you describe your product?: ")
    elif init_prompt == "quit": 
        quit = False
    else: 
        print("please add a product to continue")

