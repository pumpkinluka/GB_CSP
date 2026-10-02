# GB, Reading and Writing to Files

with open("practice.txt", 'r+') as file: # <- r+ : lets u read and write
    content = file.read()
    content = content + "\nwinnie the pooh"
    file.write(content)

with open("practice.txt", "a") as file:
    file.write("\nchiikawa is super goated")

