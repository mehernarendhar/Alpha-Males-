#Grade Filter 
def average_passing_grades(grades: list[int])->float:
    total=0
    count=0
    average=0
    for i in grades:
        if i>=50:                       
            total+=i
            count+=1
    if count==0:
            return 0.0
    average=total/count
    return float(average)

print(average_passing_grades([40, 60, 80 ,20]))
print(average_passing_grades([50,100]))
print(average_passing_grades([10,20,30]))
print(average_passing_grades([85]))
print(average_passing_grades([]))
