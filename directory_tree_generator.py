import os

for path, dirs, files in os.walk(r"C:\Users\lacho\Desktop\assignment"):
    print("The current folder is : " + path)
    for dir in dirs:
        print("Subfolder of : " + " : " + path + dir)
    for file in files:
        print("folder Inside : " + " : " + path + file)
