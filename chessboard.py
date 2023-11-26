"""
    this exercise was to create a chessboard of 1's and 0's in Python
    there is a cleaner way to acheive in numpy but I was able to work out the logic on the second day of working on the code
"""


def chessboard(num):
    for i in range(num):
        # even number row
        if i & 1 == 0:
            for j in range(num):
                if j & 1 == 0:
                    if j != num - 1:
                        print(1, end="")
                    else:
                        print(1)
                else: 
                    if j == num - 1:
                        print(0)
                    else:
                        print(0, end="")
        else:
            for j in range(num):
                if j & 1 == 0:
                    # check if last number in row
                    if j != num - 1:
                        print(0, end="")
                    else:
                        print(0)
                else:
                    if j == num - 1:
                        print(1)
                    else: 
                        print(1, end="")
# Testing the function
if __name__ == "__main__":
    chessboard(4)