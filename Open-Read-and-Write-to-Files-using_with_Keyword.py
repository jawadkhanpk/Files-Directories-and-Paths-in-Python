
# # Reading a file
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# Writing a file, mode = "w" which means write,
# It will wipe out previous content and write new text into a file
# with open("my_file.txt", mode="w") as file:
#     content = file.write("New Text")

# Writing a file, mode = "a" which means append,
# It appends text into a file. It will not disturb previous content of a file.
with open("my_file.txt", mode="a") as file:
     content = file.write("\nAppending a File Content")

