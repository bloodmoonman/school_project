from project_school_roster import student_roster
from project_school_classroom_organizer import ClassroomOrganizer
import itertools

organizer = ClassroomOrganizer()
for i in organizer:
  print(i)

seating_combination = itertools.combinations(organizer.sorted_names, 2)
for i in seating_combination:
  print(i)

for i in student_roster:
  subjects = []
  if i['favorite_subject'] == 'Math' or i['favorite_subject'] == 'Science':
    print(i['name'])
    lst = subjects.append(i['name'])
    print(lst)


print(subjects)
