# Write your solution here
from datetime import datetime, time
import csv

def cheaters() -> list:
    cheaters = set()
    start_times, end_times = {}, {}
    # fp = r'C:\Users\NUTECH\AppData\Local\tmc\vscode\mooc-programming-23\part07-14_who_cheated\src\start_times.csv'
    # fp2 = r'C:\Users\NUTECH\AppData\Local\tmc\vscode\mooc-programming-23\part07-14_who_cheated\src\submissions.csv'
    with open("start_times.csv") as f:
        for line in csv.reader(f, delimiter=";"):
            hours, minutes = line[1].split(":")
            start_times[line[0]] = time(hour=int(hours), minute=int(minutes))
    with open("submissions.csv") as f:
        for line in csv.reader(f, delimiter=";"):
            name, task, points, end_time = line
            hours, minutes = end_time.split(":")
            end_times[name] = time(hour=int(hours), minute=int(minutes))

            duration = datetime(2024,5,25,int(hours),int(minutes)) - datetime(2024,5,25,start_times[name].hour,start_times[name].minute)
            if duration.seconds > 10800:
                cheaters.add(name)
    return list(cheaters)

if __name__=="__main__":
    cheaters()
