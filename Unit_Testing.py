def DecideGrade (grade):
  txt = ''
  if grade < 50:
    txt = 'Keep Trying!'
  elif grade >= 50 and grade < 70:
    txt = 'Pass'

  return txt

StudentMark = 45
StudentGrade = DecideGrade(StudentMark)
print(StudentGrade)

#Tasks:
#1 - Complete DecideGrade
#2 - Create a list of test data
#3 - Loop through test data and check output

StudentMarks = [12,55]
for mark in StudentMarks:
  StudentGrade = DecideGrade(mark)
  print(StudentGrade)
