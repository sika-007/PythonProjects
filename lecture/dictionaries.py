"""
Dictionaries
"""

user_dict = {
  "username": "coding_with_sika",
  "name": "Nsikak",
  "age": 21
}

user_dict["married"] = True
# user_dict.pop("age")
# user_dict.clear() - makes the dictionary empty
# del user_dict - completely deletes the dictionary from memory

print(user_dict)
print(len(user_dict))
print(user_dict["username"])
print(user_dict.get("username"))

for x in user_dict:
  print(x) # Print keys
  print(user_dict[x]) # print values
  
for x, y in user_dict.items(): 
  print(x, y) # print key value pairs
  
  
user_dict2 = user_dict.copy() # Do this, if not the original dictionary is what will be assigned to user_dict2
user_dict2.pop("age")
print(user_dict)
print(user_dict2)