def order(item): 
    print("Place your order:", item)

def get_order():
    print("Preparing Order")   
    return'Order ready'



def total_price(item):
    price=25.50
    VAT=0.15
    total_price=(price+len(item))*1.15
    return total_price

My_food=input('what would you like?')
print(get_order())
   
order_total = total_price(My_food)
print(f'Total price: R{order_total:.2f}')

    
    
    








    
    

