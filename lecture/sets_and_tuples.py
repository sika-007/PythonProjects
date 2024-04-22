""" 
Sets are similar to lists but are unordered and cannot contain duplications use curly brackets
"""

my_set = {1, 2, 3, 4 ,5 ,1 , 2}
# {1, 2, 3, 4, 5}, 5

for x in my_set:
  print(x)
  
my_set.discard(3)
my_set.clear()
my_set.add(6)
my_set.update([8, 0, 8])
print(my_set, len(my_set))


""" 
Tuples are ordered like lists but unchangeable
"""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])