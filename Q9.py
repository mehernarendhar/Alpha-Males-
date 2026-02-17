#Step Sequence Generator
def generate_threes(start: int,end: int)->list[int]:
    result=[]
    if start==end:
        return []
    else:                       
        for  i in range(start,end,3):           
            result.append(i)
    return result
print(generate_threes(1,11))
print(generate_threes(0,9))
print(generate_threes(5,5))
print(generate_threes(20,10))
print(generate_threes(-5,5))
