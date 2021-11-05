# Aaron Stacey
# www.github.com/AIS05

from random import choice, randint
from math import floor
from operator import itemgetter
import json

operators = ['+', '-', '/', '*']
operator = choice(operators)

a = 1
b = 1
ans = 0
score = 0
QNum = 0
diffMultpl = 0
diff = ""
name = ""


def storeData(pscore, pname, pdiff, corrans):
    """Opens and writes json files"""
    with open('data.json', 'r+') as file:
        data = {
                'name': str(pname),
                'corrans': str(corrans),
                'score': str(pscore),
                'difficulty': str(pdiff)
        }

        file_data = json.load(file)
        file_data['scoreboard'].append(data)
        file.seek(0)
        json.dumps(file_data, file, indent=4)


def renderScoreboard():
    """Reads JSON file with the scores and displays a scoreboard"""
    with open('data.json', 'r') as file:
        scoreboard = json.load(file)['scoreboard']

    scoreboard = sorted(scoreboard, key=itemgetter('score'), reverse=True)
    for i in range(0, 9):
        try:
            print(scoreboard[i])

        except IndexError:
            break




def nameInput():
    """Username input and a welcome message"""
    global name

    print("Welcome!")
    name = str(input("What should I call you? "))
    print(f"Hello, {name}")


def diffSelect():
    """Difficulty input"""
    global diffMultpl
    global diff

    while True:
        print("Select your difficulty, higher difficulty will mean that you get bigger numbers but your score will be larger.")
        diff = str(input("Please Input 'Easy', 'Medium', 'Hard'> ")).lower()

        if diff == "easy":
            diffMultpl = 1
            break

        elif diff == "medium":
            diffMultpl = 3
            break

        elif diff == "hard":
            diffMultpl = 7
            break


def divNumGen():
    """This function generates random numbers for devision question"""
    global a
    global b
    global operator

    while True:
        a = randint(1, 12) * diffMultpl
        b = randint(1, 12) * diffMultpl

        if a % b == 0:
            break


def numGen():
    """This function generates random numbers for non-devision question"""
    global a
    global b

    if operator in ('+', '-'):
        a = randint(0, 99) * diffMultpl
        b = randint(0, 99) * diffMultpl
    elif operator == '*':
        a = randint(0, 12) * diffMultpl
        b = randint(0, 12) * diffMultpl
    else:
        divNumGen()


def printQuestion():
    """This function creates the question and makes one of the number blank"""
    global QNum

    local_a = a
    local_b = b
    local_ans = ans
    local_operator = operator
    hidden = choice(['a', 'b', 'ans', 'op'])

    if hidden == 'a':
        corAns = a
        local_a = '??'
    elif hidden == 'b':
        corAns = b
        local_b = '??'
    elif hidden == 'op':
        corAns = operator
        local_operator = '??'
    else:
        corAns = ans
        local_ans = '??'

    QNum += 1

    print("")
    print("")
    print("")
    print(f'Question {QNum}/20')
    print(f'{local_a} {local_operator} {local_b} = {local_ans}')
    print("What should be in place of ??")
    userInput(corAns)


def userInput(corAns):
    """This function takes in user input and checks if it is correct"""
    global score
    # print(corAns)
    inpt = str(input("Enter your answer "))

    if inpt == str(corAns):
        score += 1


def main():
    """Main function, starts the code"""
    global ans
    global operator

    while QNum != 20:
        operator = choice(operators)
        numGen()
        func = f'{a} {operator} {b}'
        ans = floor(eval(func))

        printQuestion()
        # print(func, f'= {ans}')

    print(f"You got {score}/20 question correct on {diff} difficulty")
    print(f"Your score is {score * diffMultpl}")

    storeData(score*diffMultpl, name, diff, score)
    print("Scoreboard:")
    renderScoreboard()


if __name__ == "__main__":
    renderScoreboard()
    nameInput()
    diffSelect()
    main()
