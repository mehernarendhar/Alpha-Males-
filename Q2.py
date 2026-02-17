#Time convertor
def convert_seconds(total_seconds: int)->str:
    minutes=total_seconds//60
    seconds=total_seconds%60
    return f'"{minutes}m {seconds}s"'   
print(convert_seconds(125))
print(convert_seconds(60))
print(convert_seconds(45))
print(convert_seconds(3600))
print(convert_seconds(0))
