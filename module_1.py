students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students_list = sorted(students)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
student_grade_one_gpa = sum(grades[0]) / len (grades[0])
student_grade_two_gpa = sum(grades[1]) / len (grades[1])
student_grade_three_gpa = sum(grades[2]) / len (grades[2])
student_grade_four_gpa = sum(grades[3]) / len (grades[3])
student_grade_five_gpa = sum(grades[4]) / len (grades[4])


gpa_dict = {}
gpa_dict.update({sorted_students_list[0]: student_grade_one_gpa, sorted_students_list[1]: student_grade_two_gpa, sorted_students_list[2]: student_grade_three_gpa, sorted_students_list[3]: student_grade_four_gpa, sorted_students_list[4]: student_grade_five_gpa})
print(gpa_dict)