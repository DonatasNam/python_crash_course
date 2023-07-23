path = 'learning_python.txt'
##
with open(path) as file_object:
    for line in file_object:
        print(line.rstrip())
##
with open(path) as file_object:     
    contents = file_object.read()

print(contents.rstrip())
##
with open(path) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python','Rust')
    print(line.rstrip())





