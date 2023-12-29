# tee ratkaisu tänne
# students_file = input("Student information: ")
# exercise_file = input("Exercises completed: ")
# exam_file = input("Exam points: ")
students_file = "students1.csv"
exercise_file = "exercises1.csv"
exam_file = "exam_points1.csv"

def points_to_grade(points: int) -> int:
    if points < 15:
        return 0
    elif points < 18:
        return 1
    elif points < 21:
        return 2
    elif points < 24:
        return 3
    elif points < 28:
        return 4
    else:
        return 5

def exercises_to_grade(exercises_completed: int) -> int:
    if exercises_completed == 40:
        return 10
    return 10 * exercises_completed // 40

students = {}

with open(students_file) as new_file:

    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        name = parts[1] + " " + parts[2].strip()
        students[parts[0]] = name

exercises = {}

with open(exercise_file) as new_file:
    
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue

        cur_sum = 0
        for i in range(1, len(parts)):
            cur_sum += int(parts[i])
        exercises[parts[0]] = cur_sum

exams = {}

with open(exam_file) as new_file:

    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        cur_sum = 0
        for i in range(1, len(parts)):
            cur_sum += int(parts[i])
        exams[parts[0]] = cur_sum
        

# for student_id, name in students.items():
#     if student_id in exams:
#         exercise_pts = exercises_to_grade(exercises[student_id])
#         print(f"{name} {points_to_grade(exams[student_id] + exercise_pts)}")
#     else:
#         print(f"{name} 0")


print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")
print(f"{'-'*25:30}{'-'*len('exec_nbr'):10}{'-'*len('exec_pts.'):10}{'-'*len('exm_pts.'):10}{'-'*len('tot_pts.'):10}{'-'*len('grade'):10}")

for student_id, name in students.items():
    exercise_pts = exercises_to_grade(exercises[student_id])
    total_pts = exams[student_id] + exercise_pts
    grade = points_to_grade(exams[student_id] + exercise_pts)

    print(f"{name:30}{exercises[student_id]:<10}{exercise_pts:<10}{exams[student_id]:<10}{total_pts:<10}{grade:<10}")

# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade     
# -------------------------     --------  --------- --------  --------  -----     
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3