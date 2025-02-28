import os

# task 1
def list_contents(path):
    print("Checking path:", path)
    if not os.path.exists(path):
        print("Path does not exist!")
        return
    
    dirs = []
    files = []
    everything = []
    
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        everything.append(item)
        if os.path.isdir(full_path):
            dirs.append(item)
        elif os.path.isfile(full_path):
            files.append(item)
    
    print("Directories:", dirs)
    print("Files:", files)
    print("Everything:", everything)

# task 2
def check_access(path):
    print("Checking access for:", path)
    print("Exists?", os.path.exists(path))
    print("Readable?", os.access(path, os.R_OK))
    print("Writable?", os.access(path, os.W_OK))
    print("Executable?", os.access(path, os.X_OK))

# task 3
def check_path(path):
    if os.path.exists(path):
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Oops! Path does not exist.")

# task 4
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The file '{filename}' has {line_count} lines.")
    except FileNotFoundError:
        print("File not found!")

# task 5
def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + "\n")
    print("Data written to", filename)

# task 6
def generate_text_files():
    for i in range(26):
        filename = f"{chr(65 + i)}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is {filename}")
        print("Created:", filename)

# task 7
def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dst:
            for line in src:
                dst.write(line)
        print("Copied contents from", source, "to", destination)
    except FileNotFoundError:
        print("Source file not found!")

# task 8
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted:", path)
        else:
            print("No permission to delete the file!")
    else:
        print("File does not exist!")
