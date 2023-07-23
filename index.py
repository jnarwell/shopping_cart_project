import random

available_items = {}
cart = []

def shop_cart():
    print('Welcome to the ultimate grocery store. Please type \'add\' to add items to your cart, \'remove\' to remove items, \'view\' to view your cart, and either \'check out\' or \'quit\' to finish shopping.')
    while True:
        action = input('Please enter action: ')
        if action.lower()=='quit' or action.lower()=='check out':
            if cart == []:
                print('Your cart is empty.')
            else:
                print('In your cart you have:')
                for item in get_cart().content:
                    print(str(item['quantity'])+' '+item['name']+'s costing $'+str((item['price']*item['quantity'])))
                print('And the total cost is $'+ str(get_cart().value))
            break
        elif action.lower() == 'add': add_item()
        elif action.lower() == 'remove': remove_item()
        elif action.lower() == 'view':
            if cart == []:
                print('Your cart is empty.')
            else:
                print('In your cart you have:')
                for item in get_cart().content:
                    print(str(item['quantity'])+' '+item['name']+'s costing $'+str((item['price']*item['quantity'])))
                print('And the total cost is $'+ str(get_cart().value))

def get_cart():
    cart_content = []
    added_duplicate = False
    for item in cart:
        for subdict in cart_content:
            if item in subdict.values():
                subdict['quantity'] += 1
                added_duplicate = True
        if added_duplicate == True: pass
        else:    
            cart_content.append({'name':get_item(item).name,'price':get_item(item).price,'quantity':1})
        added_duplicate = False
    
    cart_val = round(sum([get_item(item).price for item in cart]),2)
    def result():return cart_content, cart_val
    setattr(result,'content',cart_content)
    setattr(result,'value',cart_val)
    return result

def get_item(item_name):
    if item_name not in available_items: available_items.update({item_name:round(random.uniform(2,10),2)})
    def result():return item_name, available_items.get(item_name)
    setattr(result,'name',item_name)
    setattr(result,'price',available_items.get(item_name))
    return result

def add_item():
    item_name = input('What would you like to add? ')
    added_quant = int(input('How many of this item do you want to add? '))
    for i in range(added_quant):
        cart.append(item_name)

def remove_item():
    item_name = input('What would you like to remove? ')
    removed_quant = int(input('How many of this item do you want to remove? '))
    if removed_quant <= cart.count(item_name):
        for i in range(removed_quant):
            cart.remove(item_name)
    else:
        for i in cart.count(item_name):
            cart.remove(item_name)

shop_cart()