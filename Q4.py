#Ticket Pricer
def get_ticket_price(age: int,is_student:bool)->int:
    if age<12:
        cost=8
    elif age>65:
        cost=10
    elif age>=12 and age<=64:    
        if is_student:
            cost=12
        else:
            cost=15
    return cost
print(get_ticket_price(10,False))
print(get_ticket_price(70,True))
print(get_ticket_price(20,True))
print(get_ticket_price(25,False))
print(get_ticket_price(12,False))
