# Input a Python list of student heights
student_heights = input().split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
  total_height += height
  
print(f"total height = {total_height}")

nos = 0
for student in student_heights:
  nos += 1
  
print(f"number of students = {nos}")

average = round(total_height/nos)
print(f"average height = {average}")
