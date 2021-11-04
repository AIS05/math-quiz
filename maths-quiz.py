from random import choice, randint
from math import floor

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


def nameInput():   
    global name

    print("Welcome!")
    name =  str(input("What should I call you? "))
    print(f"Hello, {name}") 


def diffSelect():   
    global diffMultpl
    global diff

    while True:   
        print("Select your difficulty, higher difficulty will mean that you get bigger numbers but your score will be larger.")
        try:   
            diff = str(input("Please Input 'Easy', 'Medium', 'Hard'> ")).lower()
        except Exception:   
            pass

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
    global a
    global b
    global operator

    while True:   
        a = randint(1, 12)
        b = randint(1, 12)

        if a % b == 0:   
            break


def numGen():   
    global a
    global b
    global operator
    global diffMultpl

    if operator in ('+','-'):   
        a = randint(0, 99) * diffMultpl
        b = randint(0, 99) * diffMultpl
    elif operator == '*':   
        a = randint(0, 12) * diffMultpl
        b = randint(0, 12) * diffMultpl
    else:   
        divNumGen()


def printQuestion():   
    global a
    global b
    global operator
    global ans
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
    global score
    #print(corAns)
    inpt = str(input("Enter your answer "))

    if inpt == str(corAns):    
        score += 1


def main():    
    global a
    global b
    global operator
    global ans

    while QNum != 20:    
        numGen()
        func = f'{a} {operator} {b}'
        ans = floor(eval(func))

        printQuestion()
        #print(func, f'= {ans}')

    print(f"You got {score}/20 question correct on {diff} difficulty")
    print(f"Your score is {score * diffMultpl}")


if __name__ == "__main__":    
    nameInput()
    diffSelect()
    main()
