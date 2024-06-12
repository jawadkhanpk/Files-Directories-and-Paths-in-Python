import os

# Absolute path
absolute_path = "/My Drive/PROGRAMMING/Python Projects/Files-Directories-and-Paths-in-Python/my_file.txt"
print(f"Absolute Path: {absolute_path}")

# Relative path
relative_path = "my_file.txt"
print(f"Relative Path: {relative_path}")


# Check if paths exist
print(f"\nDoes absolute path exist? {os.path.exists(absolute_path)}")
print(f"Does relative path exist? {os.path.exists(relative_path)}")