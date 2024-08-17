#!/opt/homebrew/bin/python3.11

import curses
from curses import wrapper

def welcome(stdscr, red):
    height, width = stdscr.getmaxyx()
    x = (width - len("|  ____/ | | |    ||  _ |   |  ____/ ___) |    || ___ || ___)")) // 2
    y = height // 3 
    center = (width - len("Press any key to begin!")) // 2
    stdscr.clear()
    stdscr.addstr(y-5, x, "")
    stdscr.addstr(y-4, x, " ______                      ______      _                   ")
    stdscr.addstr(y-3, x, "(_____ \\                    (_____ \\    (_)                  ")
    stdscr.addstr(y-2, x, " _____) )   _ ____  ____     _____) )___ _ ____ _____  ____ ", red)
    stdscr.addstr(y-1, x, "|  ____/ | | |    \\|  _ \\   |  ____/ ___) |    \\|___ |/ ___)", red)
    stdscr.addstr(y+0, x, "| |    | |_| | | | | |_| |  | |   | |   | | | | | ____| |    ")
    stdscr.addstr(y+1, x, "|_|    |____/|_|_|_|  __/   |_|   |_|   |_|_|_|_|_____)_|    ")
    stdscr.addstr(y+2, x, "                   |_|                                       ")
    stdscr.addstr(y+3, x, "")
    stdscr.addstr(y+4, x+25, "[Deveolped by:                    ]")
    stdscr.addstr(y+4, x+40, "AmerikanischerAdler", red)
    stdscr.addstr(y+7, center, "Press any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

# Forms
def form0(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |", curses.A_DIM)
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form1(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |", curses.A_DIM)
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form2(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |", curses.A_DIM)
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form3(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |", curses.A_DIM)
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form4(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |", curses.A_DIM)
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form5(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |", curses.A_DIM)
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form6(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |", curses.A_DIM)
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form7(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |", curses.A_DIM)
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form8(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |", curses.A_DIM)
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def form9(stdscr, run, red):
    height, width = stdscr.getmaxyx()
    c = (width - len("Press ENTER to Continue")) // 2
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |", curses.A_DIM)
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.addstr(y+7, x+10, f"{run}", red)
    stdscr.addstr(y+10, c, "Press ENTER to Continue", curses.A_BOLD)
    stdscr.refresh()
    stdscr.getkey()

def get_form(stdscr, red):
    height, width = stdscr.getmaxyx()
    x = (width - len("_____________________________________________________________")) // 2
    y = height // 2 
    stdscr.clear()
    stdscr.addstr(y-8, x, "  Questions to Help You Write... ", curses.A_BOLD)
    stdscr.addstr(y-7, x, "_____________________________________________________________")
    stdscr.addstr(y-6, x, "|                                                           |")
    stdscr.addstr(y-5, x, "|     0) About Someone You Have Known or Worked With        |")
    stdscr.addstr(y-4, x, "|     1) About Someone You Have Studied or Read About       |")
    stdscr.addstr(y-3, x, "|     2) About Someone's Life as a Whole                    |")
    stdscr.addstr(y-2, x, "|     3) A Self-Evaluation                                  |")
    stdscr.addstr(y-1, x, "|     4) About a Place                                      |")
    stdscr.addstr(y+0, x, "|     5) About an Object                                    |")
    stdscr.addstr(y+1, x, "|     6) About a Work of Art                                |")
    stdscr.addstr(y+2, x, "|     7) About an Organization or Group                     |")
    stdscr.addstr(y+3, x, "|     8) About a Problem or Dilemma                         |")
    stdscr.addstr(y+4, x, "|     9) About an Abstract Concept                          |")
    stdscr.addstr(y+5, x, "|___________________________________________________________|")
    stdscr.addstr(y+6, x, "                                                             ")
    stdscr.addstr(y+7, x, "  Number: ")
    stdscr.refresh()

    while True:
        try:
            key = stdscr.getkey()
        except:
            continue

        global forum
        global max_ques

        if ord(key) == 48:
            forum = "known.txt"
            run = 0
            max_ques = 21
            form0(stdscr, run, red)
            break

        elif ord(key) == 49: 
            forum = "read.txt"
            run = 1
            max_ques = 19
            form1(stdscr, run, red)
            break

        elif ord(key) == 50: 
            forum = "life.txt"
            run = 2
            max_ques = 13
            form2(stdscr, run, red)
            break

        elif ord(key) == 51: 
            forum = "self.txt"
            run = 3
            max_ques = 16
            form3(stdscr, run, red)
            break

        elif ord(key) == 52: 
            forum = "place.txt"
            run = 4
            max_ques = 25
            form4(stdscr, run, red)
            break

        elif ord(key) == 53: 
            forum = "object.txt"
            run = 5
            max_ques = 25
            form5(stdscr, run, red)
            break

        elif ord(key) == 54: 
            forum = "art.txt"
            run = 6
            max_ques = 18
            form6(stdscr, run, red)
            break

        elif ord(key) == 55: 
            forum = "group.txt"
            run = 7
            max_ques = 18
            form7(stdscr, run, red)
            break

        elif ord(key) == 56: 
            forum = "dilemma.txt"
            run = 8
            max_ques = 21
            form8(stdscr, run, red)
            break

        elif ord(key) == 57: 
            forum = "concept.txt"
            run = 9
            max_ques = 14
            form9(stdscr, run, red)
            break

        elif ord(key) == 27:
            stdscr.nodelay(False) 
            break


def display(stdscr, text, current, header):
    height, width = stdscr.getmaxyx()
    navbar = (width - len(f"Saving to: {my_list} | Press ENTER for Next Question | Press ESC to Save & Exit")) // 2 
    num = 0

    stdscr.addstr(num+1, 5, f"{header}")
    stdscr.addstr(num+5, 5, f"{text}")
    stdscr.addstr(height-2, navbar // 2, f"Saving to: {my_list} | Press ENTER for Next Question | Press ESC to Save & Exit")

    global rep
    rep = num + 8
    for i, char in enumerate(current):
        stdscr.addstr(rep, 2+i, char)


def load_text(): 
    with open(f"./lists/{forum}", "r") as f: 
        lines = f.readlines() 
        return lines
    f.close()

def load_header(): 
    with open(f"./lists/desc/{forum}", "r") as f: 
        line = f.readline() 
        return line
    f.close()

def questionnaire(stdscr):
    stdscr.nodelay(True)

    global txt_index
    global current_text
    global target_text

    txt_index = 0
    texts = load_text()
    target_text = texts[txt_index]
    header = load_header()
    current_text = []
    height, width = stdscr.getmaxyx()
    fy = height // 2

    with open(my_list, "a") as l:
        l.write(str(header))
    l.close()

    while True:
        stdscr.clear()
        display(stdscr, target_text, current_text, header)
        stdscr.refresh()

        try:
            key = stdscr.getkey()
        except:
            continue
 
        if ord(key) == 27:
            stdscr.nodelay(False) 
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif ord(key) == 13 or ord(key) == 10 or key == curses.KEY_ENTER:
            with open(my_list, "a") as l:
                l.write("\n" + str(target_text) + "\n")
                for char in current_text:
                    l.write(str(char)) 
                l.write("\n")
            l.close()

            current_text = []
            if txt_index < max_ques - 1:
                txt_index += 1
                target_text = texts[txt_index]
            else:
                target_text = "Press ESC to Save Work"

#           Movement on ENTER
#           y, x = stdscr.getyx()
#           stdscr.move(y+1, 0)
#           global rep 
#           rep += 2

        else:
            current_text.append(key)

    with open(my_list, "a") as l:
        l.write("\n")
    l.close()


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)

    GREEN = curses.color_pair(1)
    RED = curses.color_pair(2)
    WHITE = curses.color_pair(3)
    CYAN = curses.color_pair(4)

    welcome(stdscr, RED) 
    get_form(stdscr, RED)

    height, width = stdscr.getmaxyx()
    h_middle = height // 2 
    w_middle = (width - len("Your Form has been Saved Successfully!")) // 2 
    a_middle = (width - len("Press ESC to Exit")) // 2 

    while True:
        questionnaire(stdscr)
        stdscr.addstr(h_middle, w_middle, "Your Form has been Saved Successfully!", GREEN)
        stdscr.addstr(h_middle+2, a_middle, "Press ESC to Exit", curses.A_BOLD)
        key = stdscr.getkey()
		
        if ord(key) == 27:
	        break

if __name__ == "__main__":
    global my_list
    my_list = input("Enter Name of File to Save Questionnaires to (ex. my_list.txt): ")
    wrapper(main)

