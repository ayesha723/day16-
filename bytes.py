import os
file_name = 'data.txt'


try:
    size = os.path.getsize(file_name)
    print(f"The size of '{file_name}' is {size} bytes.")
    

except FileNotFoundError:
    print("The file  does not exist.")