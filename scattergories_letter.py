import tkinter as tk
import string
import random
import time

LETTERS = list(string.ascii_uppercase)
COLORS  = ["#FF0000", "#FF3B00", "#FF7600", "#FFB100", "#FFEB00", "#D8FF00", "#9DFF00", "#62FF00", "#27FF00", "#00FF14", "#00FF4E", "#00FF89", "#00FFC4", "#00FFFF", "#00C4FF", "#0089FF", "#004EFF", "#0014FF", "#2700FF", "#6200FF", "#9D00FF", "#D800FF", "#FF00EB", "#FF00B1", "#FF0076", "#FF003B"]

class letterGenerator:
    def __init__(self, master):
        # Attributes
        self.runstatus = True
        self.letter = tk.StringVar()
        self.letter.set("A") # Initialize with "A"
        self.letter_size = 80

        # GUI
        self.master = master
        master.title("Scattergories letter sampler")
        self.label = tk.Label(master,
            text = "Click STOP to select letter:",
            font = "Calibri 20 bold"
        )
        self.label.grid(row=0)

        # Make stop button; set false initially
        self.button = tk.Button(master,
            text = 'STOP',
            justify = 'left',
            command = self.stop_cycle
        )
        self.button.grid(row=0, column=1)

        # Make button for letter loop
        self.button_update_letter = tk.Button(
            master,
            text = 'LETTER ROULETTE',
            justify = 'left',
            command = self.letterLoop
        )
        self.button_update_letter.grid(row=0,column=2)

        # LETTER LABEL
        self.letter_label = tk.Label(
            master,
            textvariable = self.letter,
            font = f"Calibri {self.letter_size}"
        )
        self.letter_label.grid(row=1, columnspan=3)

    # Method for running letter loop
    def letterLoop(self):
        index = random.randint(0, len(LETTERS) - 1)
        if self.runstatus == True:
            self.letter.set(str(LETTERS[index]))
            self.letter_label.config(
                foreground = COLORS[index],
                font = f"Calibri {self.letter_size}"
            )
            root.after(20, self.letterLoop)
        else:
            self.letter_label.config(
                foreground = 'black'
            )
            self.runstatus = True

    def stop_cycle(self):
        self.runstatus = False

root = tk.Tk()
root.rowconfigure(1, minsize = 10)
gui = letterGenerator(root)
root.mainloop()
