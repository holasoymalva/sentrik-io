import os

save_path = './data'
file_name = "general.json"

completeName = os.path.join(save_path, file_name)
print(completeName)

file1 = open(completeName, "w")
file1.write("file information")
file1.close()