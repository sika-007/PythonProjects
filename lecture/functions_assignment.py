def function(first_name, last_name, age):
  info_dict = {
    "first_name": first_name,
    "last_name": last_name,
    "age": age
  }
  return info_dict

person1 = function(first_name="Nsikak", last_name="Thomas", age=22)
print(person1)