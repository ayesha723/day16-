file_name = 'data.txt'

try:
    
    with open(file_name, 'r') as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
