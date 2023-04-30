gpa = float(input("Enter the student's GPA: "))
grade = input("Enter the student's grade: ")
grades = ["A", "B", "C", "D", "F"]
if 2.50 < gpa < 4 and grade in grades[0:2]:
    print("Eligible")
else:
    print("Ineligible")
