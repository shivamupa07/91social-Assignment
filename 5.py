new_file = open('file.txt', 'r')

final_list = []
count = 0
#creates a list containting "\n" at the end of each elements
lines = new_file.readlines()

#removes "\n" at the end of each element
for line in lines:
    final_list.append(line.strip())
    
for line in final_list:
    #replace comma with white spaces
    line = line.replace(","," ")
    line = line.split(" ")
    #remove any empty string from the list
    while("" in line):
        line.remove("")
    for word in line:
        count = count + 1
    
print(count)
