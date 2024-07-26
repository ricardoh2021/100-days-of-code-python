# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
studentCounter = 0 
height = 0 
for student in student_heights:
  height += student 
  studentCounter+= 1

print(f"total height = {height}")
print(f"number of students = {studentCounter}")
print(f"average height = {round(height/studentCounter)}")