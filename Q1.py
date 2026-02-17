#calculate_total_bill
def calculate_total_bill(amount:float,tip_percent:int)->float:
    Total=amount+(amount*(tip_percent/100))
    return round(Total,2)                           
print(calculate_total_bill(100.0,15))
print(calculate_total_bill(55.50,20))
print(calculate_total_bill(200,0))
print(calculate_total_bill(12.99,10))
print(calculate_total_bill(0,15))
