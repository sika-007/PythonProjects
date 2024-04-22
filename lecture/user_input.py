""" 
User Input
"""

first_name = input("Enter your first name: ");
days = input("How many days before your birthday? ")
day_string = "day"
if days > "1" :
  day_string = "days"
print(f"hi {first_name}, only {days} {day_string} until your birthday")