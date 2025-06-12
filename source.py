import os

# Get user input
copied_text = input("Enter the text you want to insert in the first line:\n")
folder_path = input("Enter the folder path where the files are located:\n")
target_extension = input("Enter the file extension (e.g., .txt, .py):\n")

# Ensure newline at the end of inserted text
copied_text += '\n'

# Process files
for filename in os.listdir(folder_path):
    if filename.endswith(target_extension):
        file_path = os.path.join(folder_path, filename)

        # Read original content
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Write the new content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(copied_text + original_content)

print("Text inserted successfully into all matching files.")
