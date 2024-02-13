import os

while True:
    file_name = input("Enter the file name: ")
    file_path = "./" + file_name  # Construct the file path

    if os.path.exists(file_path):
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
            lines = content.split('\n')
            num_of_lines = len(lines) - 1
            print("The number of lines in the file is:", num_of_lines)
    else:
        print("File does not exist")
