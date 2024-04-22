""" 
For and While loops
"""

""" my_list = [1, 2, 3, 4, 5]
sum_my_list = 0

for i in range(3, 6):
  print(i)
  
for i in my_list[2:4]:
  print(i)
  
for i in my_list:
  sum_my_list += i
  
print(sum_my_list) """


""" 
my_days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for x in my_days_list:
  print(f"happy {x}")
"""

i = 0

while i < 5:
  i += 1
  if i == 3:
    continue
  print(i)
  if i == 4:
    break
else: 
  print("i is now larger or equal to 5")
  