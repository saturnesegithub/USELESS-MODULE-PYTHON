def text(text):
    print(text)
def put(input):
    input(input)
def plus(a,b):
    print(a + b)
def minus(a,b):
    print(a - b)
def mult(a,b):
    print(a * b)
def div(a,b):
    print(a / b)
def power(a,b):
    print(a**b)
def pi(radius):
    print(2*3.14*radius)
def strictlist(a,b,c,d,e,f):
    [a,b,c,d,e,f]
    if (a)(b)(c)(d)(e)(f)== 0:
        print("useless.list//error: Must input 6 elements,not >6 or 6<")#USELESS_VERSION_5

#NOTE: You have to put this file in a folder with the python file you want to use this module in the same folder in order for this module to work or else it will drop an error!

import random

def text(text):

    print(text)

def plus(a,b):

    print(a + b)

def minus(a,b):

    print(a - b)

def mult(a,b):

    print(a * b)

def div(a,b):

    print(a / b)

def power(a,b):

    print(a**b)

def pi(radius):

    print(2*3.14*radius)

def privlist(a,b,c,d,e,f):

    [a,b,c,d,e,f]

def looptext(text,times):

    for i in range(int(times)):

        print(text)

def pritn(text):

  return print(text[::-1])

def type(text = ""):

    input(text)

def fruit():

    fruit = ["apple","banana","kiwi","orange","strawberry"]

    choice = random.choice(fruit)

    print(a)

def coin():

    coin = random.randint(1,2)

    if coin == 1:

        print("Heads")

    elif coin == 2:

        print("Tails")

def dna():

    while True:

        print("H__________H")

        print("_H________H_")

        print("__H______H__")

        print("___H____H___")

        print("____H__H____")

        print("_____HH_____")

        print("____H__H____")

        print("___H____H___")

        print("__H______H__")

        print("_H________H_")

def timed_dna():

    while True:

        import time

        time.sleep(0.5)

        print("H__________H")

        print("_H________H_")

        print("__H______H__")

        print("___H____H___")

        print("____H__H____")

        print("_____HH_____")

        print("____H__H____")

        print("___H____H___")

        print("__H______H__")

        print("_H________H_")

def random_note():

    print("NOTE: ")

    letters = ["C","D","E","F","G","A","B"]

    note = random.choice(letters)

    print(note)

    print("")

    print("MODIFIER:")

    choices = ["SHARP","PLUS","FLAT"]

    modifier = random.choice(modf)

    print(modifier)

def fourid(text = ""):

    a = random.randint(1,9)

    b = random.randint(1,9)

    c = random.randint(1,9)

    d = random.randint(1,9)

    id = {a,b,c,d}

    print(id)

def eight_ball(text):

    text = ""

    words = ["Yes","No","Maybe","Maybe Not","Never","Pobrably"]

    output = random.choice(words)

    print(output)

def roll_die_six():

        n = [1,2,3,4,5,6]

        choosen = random.choice(n)

        print(choosen)

def roll_die_twenty():

        n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

        choosen = random.choice(n)

        print(choosen)

def grade(grade_n):

    grade_n = int(grade_n)

    if grade_n >= 0 and grade_n < 10:

        print("F")

    elif grade_n >= 10 and grade_n < 30:

        print("D")

    elif grade_n >= 30 and grade_n < 50:

        print("C")

    elif grade_n >= 50 and grade_n < 80:

        print("B")

    elif grade_n >= 80 and grade_n <= 100:

        print("A")

    else:

        print("")

def greet():

    name = input("Who are you?: ")

    print("Hello!",name,"how are you?")

def rock_paper_scissors(inputmove = ""):

    inputmove = input("Rock, Paper or Scissors?: ")

    moves = ["Rock","Paper","Scissors"]

    choosen = random.choice(moves)

    print(choosen)

def palindrome(text):

    reversedtext = text[::-1]

    output = str(reversedtext)+str(text)

    print(output)

def duck():

    print("  __")

    print("<(o )___")

    print(" ( ._> /")

    print("  `---'")

def scream(intensity):

    if intensity == 1:

        while True:

            print("a")

    elif intensity == 2:

        while True:

            print("A")

            print("a")

    elif intensity == 3:

        while True:

            print("A")

    else:

        while True:

            print("AAAAAAAA")

def rectangle():

    num = int(input("Enter number: "))

    print("____________")

    ones_list = [1] * num

    for x in ones_list:

        print("·          ·")

    print("‾‾‾‾‾‾" + "‾‾‾‾‾‾‾" + "‾‾")

def laggen():

    while True;:

        print("   █   █   █   █   █   █   █   █   █   █   █   █   █   █")

        print("█   █   █   █   █   █   █   █   █   █   █   █   █   █   ")
