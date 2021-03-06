#Nested Lists
#Given the names and grades for each student in a class of N students,
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, 
#order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    stutend=sorted(student,key=lambda x:x[1])
    second_lowest_score = sorted(list(set([x[1] for x in student])))[1]
    desired_student = []
    for stu in student:
        if stu[1] == second_lowest_score:
            desired_student.append(stu[0])
    print("\n".join(sorted(desired_student)))
