import json

dict = {'3': "request: launch", '1': "type: java", '4': "mainClass: Demo", '5': "projectName: projects_3e31f569", '2': "name: Launch Demo"}

print("Original Dictionary:")
print(dict)
print("\nJSON data:")
print(json.dumps(dict, sort_keys = True, indent = 4))