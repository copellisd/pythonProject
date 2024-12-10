import os

file_name="datta.txt"
content="he is my god"

with open(file_name,"w")  as file:
    file.write(content)

with open(file_name,"r") as file:
    content2=file.read()
    print(content2)

os.chdir("desktop")