new_file = open('file.txt', 'r')

final_list = []

#creates a list containting "\n" at the end of each elements
lines = new_file.readlines()

#removes "\n" at the end of each element
for line in lines: 
    final_list.append(line.strip()) 
    
print(final_list)