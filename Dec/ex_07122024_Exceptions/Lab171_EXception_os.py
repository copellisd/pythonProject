import os
try:
 full_path=os.getcwd()
 print(full_path)
 full_path_file=full_path+"/example.txt"
 print(full_path_file)

 file=open(full_path_file)
except Exception as e:
    print("file not found ex,find the path or create file")
finally:
  print("this code is executed any  how")