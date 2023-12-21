# Write your solution 
def add_student(database: dict, student: str) -> None:
    database[student] = []                
        
def average_grade(database: dict, student: str) -> float:
    _sum = 0
    for course in database[student]:
        name, grade = course
        _sum += grade
    return _sum / len(database[student])


def print_student(database: dict, student: str) -> None:
    if student not in database:
        print(f"{student}: no such person in the database")
    else: 
        print(f"{student}: ")
        if len(database[student]) == 0:
            print(" no completed courses")
        else:
            print(f" {len(database[student])} completed courses:")
            for course in database[student]:
                name, grade = course
                print(f"  {name} {grade}")
            print(f" average grade {average_grade(database, student)}")

def add_course(database: dict, student: str, course_info: tuple) -> None:
    cur_name, cur_grade = course_info
    if cur_grade == 0:
        return

    new_course = (cur_name, cur_grade)
    for course in database[student]:
        name, grade = course

        if cur_name == name:
            if cur_grade > grade:
                database[student].remove(course)
                database[student].append(new_course)
            return

    # student hasn't completed this course yet                     
    database[student].append(new_course)

# def most_completed(database: dict) -> tuple:
#     most = {}
#     for student in database:
#         most[student] = len(database[student])

#     ans = ""
#     times = 0
#     for name in most:
#         if most[name] > times:
#             times = most[name]
#             ans = name
#     return (ans, times)

# def best_average(database: dict) -> tuple:
#     student_avgs = {}
#     for name in database:
#         student_avgs[name] = average_grade(database, name)
    
#     ans, avg = "", 0
#     for student in student_avgs:
#         if student_avgs[student] > avg:
#             ans = student
#             avg = student_avgs[student]
#     return (ans, avg)

def summary(database: dict) -> None:
    print(f"students {len(database)}")

    most = {}
    for student in database:
        most[student] = len(database[student])

    ans, times = "", 0
    for name in most:
        if most[name] > times:
            times = most[name]
            ans = name
    
    print(f"most courses completed {times} {ans}")

    student_avgs = {}
    for name in database:
        student_avgs[name] = average_grade(database, name)
    
    res, avg = "", 0
    for student in student_avgs:
        if student_avgs[student] > avg:
            res = student
            avg = student_avgs[student]
    
    print(f"best average grade {avg} {res}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    
    
    add_course(students, "Peter", ("Software Development Methods", 5))
    summary(students)

   
    # database = {
    #     "Peter" : [
    #          ("Introduction to Programming", 1),
    #          ("Advanced Course in Programming", 1)
    #          ("Data Structures and Algorithms", 1)
    #     ],

    #     "Eliza" : [
    #         { "Introduction to Programming" : 5},
    #         { "Introduction to Computer Science" : 4}
    #     ]
    # }