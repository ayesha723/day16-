count = 'data.txt'

try:
    
    with open(count, 'r') as file:
        lines = file.read()

    print(f"the number of lines in  content is {len (lines)}.")
except FileNotFoundError:
    print(f"The file '{count}' does not exist.")
