import os

def read_file_as_string(script_dir, file_name):
    try:
        # Get the directory of the current Python script

        # Construct the file path using os.path.join
        file_path = os.path.join(script_dir, file_name)

        # Open and read the file
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


# script_dir = os.path.dirname(__file__)
# file_name = "context.txt"
# file_content = read_file_as_string(script_dir, file_name)
# print(file_content)