from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from functools import partial
import random


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\CodSoft\Tasks\Rock-Paper-Scissor\assets\frame0")
score = 0

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def buttonClicked(userChoice):
    global score
    choices = ['rock', 'paper', 'scissor']
    computerChoice = random.choice(choices)
    computerChoiceButton['file'] = relative_to_assets(f'{computerChoice}.png')
    
    
    if userChoice == 'rock':
        if computerChoice == 'rock':
            canvas.itemconfig(label1, text='Tie', fill='yellow')
        elif computerChoice == "paper":
            canvas.itemconfig(label1, text='Computer Wins', fill='red')
            score = 0
        else:
            canvas.itemconfig(label1, text='User Wins', fill='green')
            score += 1
    elif userChoice == 'paper':
        if computerChoice == 'rock':
            canvas.itemconfig(label1, text='User Wins', fill='green')
            score += 1
        elif computerChoice == "paper":
            canvas.itemconfig(label1, text='Tie', fill='yellow')
        else:
            canvas.itemconfig(label1, text='Computer Wins', fill='red')
            score = 0
    else:
        if computerChoice == 'rock':
            canvas.itemconfig(label1, text='Computer Wins', fill='red')
            score = 0
        elif computerChoice == "paper":
            canvas.itemconfig(label1, text='User Wins', fill='green')
            score += 1
        else:
            canvas.itemconfig(label1, text='Tie', fill='yellow')
    canvas.itemconfig(label2, text=f'Score: {score}')


window = Tk()

window.geometry("829x664")
window.configure(bg = "#FFFFFF")
window.title('Rock Paper Scissor Game')


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 664,
    width = 829,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    76.0,
    18.0,
    anchor="nw",
    text="Rock - Paper - Scissor",
    fill="#000000",
    font=("Kavoon Regular", 64 * -1)
)

label1 = canvas.create_text(
    215.0,
    105.0,
    anchor="nw",
    text="Result",
    fill="#000000",
    font=("Kavoon Regular", 64 * -1)
)

label2 = canvas.create_text(
    215.0,
    180.0,
    anchor="nw",
    text="Score: 0",
    fill="#000000",
    font=("Kavoon Regular", 20 * -1)
)

canvas.create_rectangle(
    413.00000762939453,
    280.0,
    416.31292724609375,
    580.9910888671875,
    fill="#000000",
    outline="")

canvas.create_text(
    118.0,
    205.0,
    anchor="nw",
    text="Your Choice",
    fill="#042CFF",
    font=("Kavoon Regular", 36 * -1)
)

canvas.create_text(
    472.0,
    205.0,
    anchor="nw",
    text="Computer Choice",
    fill="#042CFF",
    font=("Kavoon Regular", 36 * -1)
)

rockButton = PhotoImage(
    file=relative_to_assets("rock.png"))
button_1 = Button(
    image=rockButton,
    borderwidth=0,
    highlightthickness=0,
    command=partial(buttonClicked, 'rock'),
    relief="flat"
)
button_1.place(
    x=80.0,
    y=293.0,
    width=273.0,
    height=80.0
)

computerChoiceButton = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=computerChoiceButton,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_2.place(
    x=484.0,
    y=392.0,
    width=273.0,
    height=79.0
)

paperButton = PhotoImage(
    file=relative_to_assets("paper.png"))
button_3 = Button(
    image=paperButton,
    borderwidth=0,
    highlightthickness=0,
    command=partial(buttonClicked, 'paper'),
    relief="flat"
)
button_3.place(
    x=80.0,
    y=391.0,
    width=273.0,
    height=80.0
)

scissorButton = PhotoImage(
    file=relative_to_assets("scissor.png"))
button_4 = Button(
    image=scissorButton,
    borderwidth=0,
    highlightthickness=0,
    command=partial(buttonClicked, 'scissor'),
    relief="flat"
)
button_4.place(
    x=80.0,
    y=489.0,
    width=273.0,
    height=80.0
)

canvas.create_rectangle(
    0.0,
    608.0,
    829.0,
    664.0,
    fill="#00095F",
    outline="")

canvas.create_text(
    176.0,
    616.0,
    anchor="nw",
    text="Developed by Sufiyaan Usmani",
    fill="#FFFFFF",
    font=("Kavoon Regular", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
