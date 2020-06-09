#!python
import tkinter as tk
import string
import random
import time
import winsound

LETTERS = list(string.ascii_uppercase)
COLORS  = ["#FF0000", "#FF3B00", "#FF7600", "#FFB100", "#FFEB00", "#D8FF00", "#9DFF00", "#62FF00", "#27FF00", "#00FF14", "#00FF4E", "#00FF89", "#00FFC4", "#00FFFF", "#00C4FF", "#0089FF", "#004EFF", "#0014FF", "#2700FF", "#6200FF", "#9D00FF", "#D800FF", "#FF00EB", "#FF00B1", "#FF0076", "#FF003B"]

class letterGenerator:
    def __init__(self, master):
        # Attributes
        self.runstatus = True
        self.letter = tk.StringVar()
        self.letter.set("A") # Initialize with "A"
        self.letter_size = 200
        self.letter_speed = 20

        # GUI
        self.master = master
        master.title("Scattergories letter sampler")
        self.label = tk.Label(master,
            text = "Click STOP\nto select letter:",
        )
        self.label.grid(row=0, columnspan=3)

        # Make stop button; set false initially
        self.button = tk.Button(master,
            text = 'STOP',
            justify = 'left',
            command = lambda:[self.stop_cycle()],
        )
        self.button.grid(row=1, column=0)

        # Make button for letter loop
        self.button_update_letter = tk.Button(
            master,
            text = 'LETTER ROULETTE',
            justify = 'left',
            command = lambda:[self.start_cycle(), self.item_reel(), self.letterLoop()],
        )
        self.button_update_letter.grid(row=1,column=1)

        # LETTER LABEL
        self.letter_label = tk.Label(
            master,
            textvariable = self.letter,
            font = (f"{self.letter_font}", self.letter_size)
        )
        self.letter_label.grid(row=2, columnspan=3)

    # Method for running letter loop
    def letterLoop(self):
        index = random.randint(0, len(LETTERS) - 1)
        if self.runstatus == True:
            self.letter.set(str(LETTERS[index]))
            self.letter_label.config(
                foreground = COLORS[index],
                font = (f"{self.letter_font}", self.letter_size)
            )
            self.master.after(self.letter_speed, self.letterLoop)
        else:
            self.letter_label.config(
                foreground = COLORS[index]
            )
            self.master.after(self.letter_speed, self.letterLoop)


    def start_cycle(self):
        self.runstatus = True
        self.letter_speed = 20
    def stop_cycle(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
        winsound.PlaySound('sound/smw_course_clear.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        self.runstatus = False
        self.letter_speed = 425

    def item_reel(self):
        winsound.PlaySound('sound/itemreel.wav', winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)

def letter_generator():
    root = tk.Tk()
    root.rowconfigure(1, minsize = 10)
    gui = letterGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    letter_generator()
