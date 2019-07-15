#import random 


#def rand(start, end, str): 
    #res = []

    #for r in range(str): 
        #res.append(random.randint(start, end))

        #return res

#str = 'r', 'y', 'g', 'b'
#start = 'r'
#end = 'y'
#print(rand(start, end, str))

import tkinter as tk
#import color_blocks

class color_string: 
    def __init__(self, parent): 
        self.parent = parent
        self.canvas = tk.Canvas(parent)
        self.draw_board()
    def draw_board(self): 
        self.canvas = tk.canvas(self.parent, HEIGHT = 600, WIDTH = 800)
        self.canvas.pack()
        #self.squares()

class SelfSquares():
    def __init__(self,sprites, input_dict):
        self.sprites = sprites
        self.input = input_dict

        # Show Dull Red
        
        self.dull_red = dull_red(self.input)
        self.sprites.add(self.dull_red)

        # Show Dull Green

        self.dull_green = dull_green(self.input)
        self.sprites.add(self.dull_green)

        # Show Dull Blue

        self.dull_blue = dull_blue(self.input)
        self.sprites.add(self.dull_blue)

        # Show Dull Yellow

        self.dull_yellow = dull_yellow(self.input)
        self.sprites.add(self.dull_yellow)
    
    def animate(self, idx = 0)
        c = self.pattern[idx]
        self.canvas.itemconfig(self.squares[c], fill= self.light[c], outline = self.light[c])
        self.parent.after(1000, lambda: self.canvas.itemconfig(self.squares.[c],
        fill = self.dark[c], outline = self.dark[c]))

        idx += 1
        if idx < len(self.pattern): 
        self.parent.after(1000, lambda: self.animate(idx))
    else: 
        self.canvas.bind('<1>', self.select)

def select(self, event=None): 
    id = self.canvas.find_withtage("current")[0]
    color = self.ids[id]
    self.selections += color
    self.canvas.itemconfig('current', fill = self.light[color, outline=self.light[color])
    self.parent.after(1000, lambda: self.canvas.itemconfig(id, fill = self.dark[color], outline = self.dark[color]))
    if self.pattern == self.selections: 
        self.pattern += random.choice('rgby')
        self.selections = ''
        self.high_score = max(self.high_score, len(self.pattern))
        self.animate()
    elif self.pattern[len(self.selections)-1] != color: 
        self.canvas.unbind()
        self.parent.after(2000, lambda: self.status.config(text = ''))
        self.parent.after(2000, self.draw_board)
        print(self.pattern, self.selections)
def score(self, event=None): 
    self.status.config(text=self.high_score)
    self.parent.after(2000, lambda: self.status.config(text = ''))


root = tk.Tk()
color_string = color_string(root)
root.mainloop()