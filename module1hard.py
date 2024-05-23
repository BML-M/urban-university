grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Алексей', 'Иван', 'Максим', 'Наталья', 'Екатерина'}

average_grades = {}
for index, student in enumerate(students):
    grades_sum = sum(grades[index])
    average_grade = grades_sum / len(grades[index])
    average_grades[student] = round(average_grade, 2)

print(average_grades)
