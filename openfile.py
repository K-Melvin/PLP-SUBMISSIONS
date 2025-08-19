#File Read & Write Challenge 
file = open("Week 4 .pdf", "w")
file.write("Hello, World, This is amazing!")
file = open("Week 4 .pdf", "r")
data = file.read()
print(data)
file = open("Week 4 .pdf", "a")
file.write("It's a cold day!")

#Error Handling Lab 
try:
    with open("Week 4 .pdf", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")