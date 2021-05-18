import random

# Index position for products characteristics
TYPE = 0
PRICE = 1
SIZE = 2
COLOR = 3

# Products characteristics
Product_Types = ('Hoodie', 'Shirt', 'Jacket', 'Hat', 'Jeans', 'Shorts', 'Vest', 'Coat')
Product_Prices = (20,        15,       26,      8,     22,       18,      15,     28)
Product_Sizes = ('S', 'M', 'L', 'XL', 'XXl')
Product_Colors = ('Black', 'White', 'Red', 'Green', 'Blue', 'Cyan')

# Store products
Products = []


def show_all_products():
    # Print All the product in the store
    for product in Products:
        print(f'{product[TYPE]}, size: {product[SIZE]}, color: {product[COLOR]}, priced at: ${product[PRICE]}')
    print()


def generate_random_products(amount_of_products):
    for product in range(amount_of_products):
        # Generate a random set of product characteristics
        random_product = random.randint(0, 7)
        random_size = random.randint(0, 4)
        random_color = random.randint(0, 5)

        # create a product like ['Shirt', 15, 'L', 'White']
        # random type, size, color, with the price depending on the product type
        temp_product = [Product_Types[random_product],
                        Product_Prices[random_product],
                        Product_Sizes[random_size],
                        Product_Colors[random_color]]

        # append the product the the Products list
        Products.append(temp_product)


def add_single_product(product_type, product_size, product_color):
    # create the product with given parameters
    temp_product = [product_type,
                    Product_Prices[Product_Types.index(product_type)],
                    product_size,
                    product_color]

    # append the product the the Products list
    Products.append(temp_product)


def change_price(target_product, target_price):
    price_changed = False
    for product in Products:
        # if we found the product that's requested, change it's price to the given value
        if product[TYPE] == target_product:
            product[PRICE] = target_price
            price_changed = True

    # if there are more products of the same type, print only once
    if price_changed:
        print(f'* The price for {target_product} is now ${target_price} * ')
    else:
        print('* The specified product is not available *')


def check_stock_quantity(target_product):
    stock_quantity = 0
    for product in Products:
        if product[TYPE] == target_product:
            stock_quantity += 1

    print(f'* The stock quantity of {target_product} is {stock_quantity} *')
    print()


def sell_product(target_product, target_size, target_color):
    product_found = False
    for product in Products:
        # check if the requested product is indeed in stock
        if product[TYPE] == target_product and product[SIZE] == target_size and product[COLOR] == target_color:
            Products.remove(product)
            product_found = True
            print(f'* {product[COLOR]} {product[TYPE]} was sold for ${product[PRICE]} *')
            # We found a specified product, now exit
            return

    # if the product is not found, inform the user
    if not product_found:
        print("* The requested product is not available *")


def search_for(target_product):
    print(f'* Any {target_product} is priced at ${Product_Prices[Product_Types.index(target_product)]} *')
    check_stock_quantity(target_product)
    for product in Products:
        if product[TYPE] == target_product:
            print(f'{product[TYPE]}, size: {product[SIZE]}, color: {product[COLOR]}')
    print()


def sell_latest_product():
    Products.pop()


def restock_multiple_products(product_amount, product_type, product_size, product_color):
    for product in range(product_amount):
        # create the product with given parameters
        temp_product = [product_type,
                        Product_Prices[Product_Types.index(product_type)],
                        product_size,
                        product_color]

        # append the product the the Products list
        Products.append(temp_product)


if __name__ == '__main__':

    # IF at any point, a function does not find the specified product,
    # run the program again, or generate a larger number of products

    print('---Generate Products---')
    # Insert as a parameter, the number of random products to create
    # For better visualisation, keep this number small. But it can be used a big number like 1000 as well.
    generate_random_products(10)
    show_all_products()

    print('---Add a white shirt with size M---')
    # Specify the type of product, size and color. The price is inserted automatically
    add_single_product('Shirt', 'M', 'White')
    show_all_products()

    print('---Change the price for Jeans---')
    # Change the price for ALL the specified products
    change_price('Jeans', 26)
    show_all_products()

    print('---Checking Stock---')
    # Check how many products of the specified type are present in stock
    check_stock_quantity('Hoodie')

    print('---Selling a specified product---')
    sell_product('Shirt', 'M', 'White')
    show_all_products()

    print('---Show all the specified products in the store---')
    search_for('Vest')

    print('---Sell the latest product in the store---')
    sell_latest_product()
    show_all_products()

    print('---Restock multiple products of same type---')
    # Specify the amount of products to be added, Type, Size and Color
    restock_multiple_products(5, 'Jacket', 'L', 'White')
    show_all_products()

    print('---Selling a specified product---')
    sell_product('Jacket', 'L', 'White')
    show_all_products()

