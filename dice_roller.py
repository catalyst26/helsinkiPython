# Write your solution here
from random import choice

def roll(die: str) -> int:
    if die == "A":
        return choice([3,3,3,3,3,6])
    elif die == "B":
        return choice([2,2,2,5,5,5])
    elif die == "C":
        return choice([1,4,4,4,4,4])


def play(die1: str, die2: str, times: int) -> tuple:
    score1 = score2 = ties = 0
    for i in range(times):
        player1 = roll(die1)
        player2 = roll(die2)

        if player1 > player2: score1 += 1
        elif player1 < player2: score2 += 1
        else: ties += 1
    return (score1, score2, ties)

    

if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)