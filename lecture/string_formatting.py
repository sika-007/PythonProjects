""" 
String formatting
"""

first_name = "Nsikak"
last_name = "Thomas"
print("Hi " + first_name)
print(f"Hi {first_name}")

sentence = "hi {} {}"
print(sentence.format(first_name, last_name))

# print(sentence.format(first_name))
