def calculate_homework(homework_assignment): 
  sum_of_grades = 0
  for score in homework_assignment.values():
    sum_of_grades += score
  final_grade = sum_of_grades/len(homework_assignment)
  print(round(final_grade, 2))