from tkinter import *
import tkinter.messagebox


def quit_gamebtn(e):
    ans = tkinter.messagebox.askokcancel('Confirm Exit', 'Are you sure want to exit Sudoku?')
    if ans:
        quit()


def quit_game():
    ans = tkinter.messagebox.askokcancel('Confirm Exit', 'Are you sure want to exit Sudoku?')
    if ans:
        quit()


def new_game(e):
    pass


def practice_game(e):
    pass


def hint(e):
    pass


def save(e):
    pass


def reset(e):
    pass


def stats(e):
    pass


def single_mode(e):
    pass


def computer_mode(e):
    pass


def dual_player(e):
    pass


def themes(e):
    pass


def sound_on_off(e):
    pass


def logout(e):
    pass


def tips(e):
    pass


def get_help(e):
    pass


def update(e):
    pass


def contact_us(e):
    pass


def about_us(e):
    pass


root = Tk()
root.title("Sudoku Game")
root.geometry("300x500+0+0")

main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New Game...", command=new_game)
file_menu.add_command(label="Practice Game ", command=practice_game)
file_menu.add_separator()
file_menu.add_command(label="Hint", command=hint)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Reset", command=reset)
file_menu.add_command(label="Stats...", command=stats)
file_menu.add_separator()

# Settings Menu in File Menu
settings_menu = Menu(file_menu)
file_menu.add_cascade(label="Settings", menu=settings_menu)
file_menu.add_separator()
file_menu.add_command(label="Log Out...", command=logout)
file_menu.add_command(label="Quit", command=quit_game)

# Playing Menu in Setting Menu
playing_menu = Menu(settings_menu)
settings_menu.add_cascade(label="Playing Mode", menu=playing_menu)
playing_menu.add_command(label="Single Player", command=single_mode)
playing_menu.add_command(label="Computer Mode", command=computer_mode)
playing_menu.add_command(label="Dual Player", command=dual_player)
settings_menu.add_command(label="Themes", command=themes)
settings_menu.add_command(label="Sound ON/OFF", command=sound_on_off)

# Help Menu in File Menu
help_menu = Menu(main_menu)
main_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Tip of the Day", command=tips)
help_menu.add_command(label="Help", command=get_help)
help_menu.add_separator()
help_menu.add_command(label="Check for update", command=update)
help_menu.add_separator()
help_menu.add_command(label="Contact Us", command=contact_us)
help_menu.add_command(label="About Us", command=about_us)

# Main Window
top = Frame(root)
bottom = Frame(root)
top.pack(expand=300)

button_1 = Button(top, text=" New Game ")
button_2 = Button(top, text=" Practice Game ")
button_3 = Button(top, text=" Stats ")
button_5 = Button(top, text="Sound ON/OFF")
button_6 = Button(top, text="Quit")

button_1.bind("<Button-1>", new_game)
button_2.bind("<Button-1>", practice_game)
button_3.bind("<Button-1>", stats)
button_5.bind("<Button-1>", sound_on_off)
button_6.bind("<Button-1>", quit_gamebtn)

button_1.pack(pady=10, fill=X, ipady=3)
button_2.pack(pady=10, fill=X, ipady=3)
button_3.pack(pady=10, fill=X, ipady=3)
button_5.pack(pady=10, fill=X, ipady=3)
button_6.pack(pady=10, fill=X, ipady=3)

if __name__ == '__main__':
    root.mainloop()
