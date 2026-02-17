#Fruit Stand Inventory
def count_inventory(fruit_list: list[str])->dict[str,int]:
    frequency = {}
    for fruit in fruit_list:
        if fruit in frequency:
            frequency[fruit]+=1
        else:
            frequency[fruit]=1
    return frequency
print(count_inventory(["apple","banana","apple","cherry"]))
print(count_inventory(["orange","orange"]))
print(count_inventory(["grape"]))
print(count_inventory([]))
print(count_inventory(["Apple","apple",]))
