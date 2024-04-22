"""
Functions
"""
def my_function():
  print("This is within my function")
  
def print_my_name(first_name, last_name):
  print(f"Hello {first_name} {last_name}")
  
def print_color_red():
  color = "red";
  print(color)


color = "Blue"
print(color)
my_function()
print_my_name(first_name="Nsikak", last_name="Success")
print_color_red()

def print_numbers(highest_number, lowest_number):
  print(highest_number, lowest_number)
  
def multiply_numbers(a, b):
  return a * b
multiplication = multiply_numbers(4, 10)

def print_list(list_of_numbers):
  for x in list_of_numbers:
    print(x)
  
print_numbers(10, 3)
print(multiplication)
print_list([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])

def add_tax_to_item(cost_of_item):
  current_tax_rate = .03
  return (cost_of_item * current_tax_rate)

def buy_item(cost_of_item):
  return cost_of_item + add_tax_to_item(cost_of_item)

final_cost = buy_item(50)
print(final_cost)