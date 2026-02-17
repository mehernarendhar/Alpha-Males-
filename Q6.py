#Temperature Converter
def convert_temperature(value:float,unit:str)-> float | str:
    if unit=="F":
        C = (value-32)*(5/9)
        return round(float(C),1)
    elif unit=="C":
        F = (value*9/5)+32              
        return round(float(F),1)           
    else:
        return '"Ivalid Unit"'
    
print(convert_temperature(0,'C'))
print(convert_temperature(100,'F'))
print(convert_temperature(100,'C'))
print(convert_temperature(-40,'F'))
print(convert_temperature(25,'k'))
