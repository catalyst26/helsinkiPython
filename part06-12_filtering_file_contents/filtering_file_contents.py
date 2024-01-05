# Write your solution here
def filter_solutions():
    with open("correct.csv", "w") as new_file:
        pass
    with open("incorrect.csv", "w") as new_file:
        pass
    solutions = []

    with open("solutions.csv") as new_file:
        
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            
            name, problem, result = parts
            # parse problem string to seperate numbers and sign
            first = second = 0
            number = sign = ""
            for c in problem:
                if c not in "+-":
                    number += c
                else:
                    sign = c
                    first = int(number)
                    number = ""
            second = int(number)

            solutions.append([name, first, sign, second, int(result)])
    
    for solution in solutions:
        name, first, sign, second, result = solution

        cur_result = 0
        if sign == "+":
            cur_result = first + second
        else:
            cur_result = first - second
        
        if cur_result != result:
            with open("incorrect.csv", "a") as new_file:
                new_file.write(f"{name};{first}{sign}{second};{result}\n")
        else:
            with open("correct.csv", "a") as new_file:
                new_file.write(f"{name};{first}{sign}{second};{result}\n")

if __name__ == "__main__":
    filter_solutions()
    filter_solutions()
    filter_solutions()
    filter_solutions()
    filter_solutions()




