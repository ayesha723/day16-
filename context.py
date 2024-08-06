file_name = 'data.txt'


try:
    with open(file_name, 'r') as file:
        content=file.read()
    print("file content")
    print(content)

except FileNotFoundError:
    print(f"The file  does not exist.")