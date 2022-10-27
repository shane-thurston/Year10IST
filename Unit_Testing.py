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
#1 - Complete DecideGrade 70-84 Credit 85-100 Distinction
#2 - Create a list of test data
#3 - Loop through test data and check output
#4 - authenticate valid marks through input
#5 - option to loop a set number of times. Return mark and feedback.

