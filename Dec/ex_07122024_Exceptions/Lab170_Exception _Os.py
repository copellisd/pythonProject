import os

print(os.getcwd())
files=os.listdir('/Users/prave/PycharmProjects/PyATB5xLearning/')
print(f"files in the directory :{files}")
#create a directory
#os.mkdir('test2')

file_exist=os.path.exists("testdata.txt")
print(file_exist)