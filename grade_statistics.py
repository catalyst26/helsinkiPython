# Write your solution here
def convert_exercise_pts(exercise_points):
    if exercise_points == 100:
        return 10
    return exercise_points // 10

def convert_exam_exercise_pts_to_grade(exam_pts, exercise_pts):
    combined_pts = exam_pts + convert_exercise_pts(exercise_pts)

    if exam_pts < 10 or combined_pts <= 14:
        return 0
    elif combined_pts <= 17:
        return 1
    elif combined_pts <= 20:
        return 2
    elif combined_pts <= 23:
        return 3
    elif combined_pts <= 27:
        return 4
    else:
        return 5

def average(total, num):
    return f"{(total / num):.1f}"

def stats_to_percent(my_list, num):
    passed = [x for x in my_list if x > 0]
    decimal = len(passed) / len(my_list)
    percentage = float(decimal * 100)

    return f"{percentage:.1f}"

def distribution(my_list):
    i = 5
    while i >= 0:
        print(f"{i}: {my_list.count(i) * '*'}")
        i -= 1

def main():

    statistics = []
    number_of_students = 0
    sum_pts = 0

    while True:

        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break

        user_exam_pts, user_exercise_pts = user_input.split()

        sum_pts += (int(user_exam_pts) + convert_exercise_pts(int(user_exercise_pts)))
        number_of_students += 1
        
        statistics.append(convert_exam_exercise_pts_to_grade(int(user_exam_pts), int(user_exercise_pts)))
    
    print("Statistics: ")
    print(f"Points average: {average(sum_pts, number_of_students)}")
    print(f"Pass percentage: {stats_to_percent(statistics, number_of_students)}")
    print("Grade distribution: ")
    distribution(statistics)

main()





    