file_name = 'data.txt'
text_to_append = 'End of file\n'

try:
    with open(file_name, 'a') as file:
        file.write(text_to_append)
    print(f"Text '{text_to_append.strip()}' appended to '{file_name}'.")
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")
