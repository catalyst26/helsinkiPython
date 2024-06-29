# Write your solution here
from datetime import datetime, time
import csv

def cheaters() -> list:
    cheaters = set()
    start_times, end_times = {}, {}
    # fp = r'C:\Users\NUTECH\AppData\Local\tmc\vscode\mooc-programming-23\part07-15_who_cheated_2\src\start_times.csv'
    # fp2 = r'C:\Users\NUTECH\AppData\Local\tmc\vscode\mooc-programming-23\part07-15_who_cheated_2\src\submissions.csv'
    with open("start_times.csv") as f:
        for line in csv.reader(f, delimiter=";"):
            hours, minutes = line[1].split(":")
            start_times[line[0]] = time(hour=int(hours), minute=int(minutes))
    with open("submissions.csv") as f:
        for line in csv.reader(f, delimiter=";"):
            name, task, points, end_time = line
            hours, minutes = end_time.split(":")
            if name in end_times:
                end_times[name].append((task, points, time(hour=int(hours), minute=int(minutes))))
            else:
                end_times[name] = [(task, points, time(hour=int(hours), minute=int(minutes)))]
            # end_times[name] = (task, points, time(hour=int(hours), minute=int(minutes)))

            duration = datetime(2024,5,25,int(hours),int(minutes)) - datetime(2024,5,25,start_times[name].hour,start_times[name].minute)
            if duration.seconds > 10800:
                cheaters.add(name)
    return start_times, end_times

def final_points() -> dict:
    # returns start and end times dicts from previous exercise
    
    st, et = cheaters()
    """
        tasks are numbered 1 - 8
        submission grade is from 0 - 6 points
        task, points, end time

        for each name in st, find all submissions in et, filter by task
        compare end times in the dict, if valid time then record highest points
        arto = {
        # list of submission tuples for each task
            1 : [(4, 3, 18:55), (1, 6, 19:02), (3, 3, 18:45)],
            2 : [(1 ,5, 19:22)],
            3 : [],
            ...
            8 : [(2, 2, 20:00)]
        }
    """
    task_and_submissions = {}
    for student, start_time in st.items():
        for triplet in et[student]:
            task, points, end_time = triplet
            # check if this is a valid submission
            duration = datetime(2024, 5, 25, end_time.hour, end_time.minute) - datetime(2024, 5, 25, start_time.hour, start_time.minute)
            if duration.seconds > 10800: continue
            # valid submission, add to the dictionary
            if student in task_and_submissions:
                if task in task_and_submissions[student]:
                    # multiple submissions for same task
                    task_and_submissions[student][task].append((task, points, end_time))
                else:
                    # first submission for this task for this student
                    task_and_submissions[student][task] = [(task, points, end_time)]
            else:
                task_and_submissions[student] = {task : []}
                task_and_submissions[student][task].append((task, points, end_time))

    final_exam_points = {}
    
    for student, task in task_and_submissions.items():
        for task_num, submissions in task.items():
            task_max_point = 0
            for triplet in submissions:
                task, points, end_time = triplet
                task_max_point = max(task_max_point, int(points))
            if student in final_exam_points:
                final_exam_points[student] += task_max_point
            else: 
                final_exam_points[student] = task_max_point
    
    return final_exam_points


if __name__=="__main__":
    final_points()